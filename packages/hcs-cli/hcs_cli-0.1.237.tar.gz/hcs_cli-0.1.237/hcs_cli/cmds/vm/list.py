"""
Copyright 2023-2023 VMware Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import click
import hcs_cli.service.admin as admin
import hcs_core.sglib.cli_options as cli
from hcs_core.ctxp import recent, util
import hcs_core.ctxp.cli_options as common_options
from hcs_core.util import duration
from hcs_cli.support.constant import provider_labels


def _colorize(data: dict, name: str, mapping: dict):
    s = data[name]
    c = mapping.get(s)
    if c:
        if isinstance(c, str):
            data[name] = click.style(s, fg=c)
        else:
            color = c(data)
            data[name] = click.style(s, fg=color)


def _format_vm_table(data):
    for d in data:
        updatedAt = d["updatedAt"]
        d["stale"] = duration.stale(updatedAt)

        _colorize(
            d,
            "lifecycleStatus",
            {
                "DELETING": "bright_black",
                "ERROR": "red",
                "PROVISIONING": "blue",
                "PROVISIONED": "green",
                "MAINTENANCE": "yellow",
            },
        )

        _colorize(
            d,
            "powerState",
            {
                "PoweredOn": "green",
                "PoweringOn": "blue",
                "PoweredOff": "bright_black",
                "PoweringOff": "blue",
            },
        )

        _colorize(
            d,
            "agentStatus",
            {"AVAILABLE": "green", "ERROR": lambda d: "bright_black" if d["powerState"] != "PoweredOn" else "red"},
        )

        _colorize(
            d,
            "sessionPlacementStatus",
            {
                "AVAILABLE": "green",
                "UNAVAILABLE": lambda d: "bright_black" if d["powerState"] != "PoweredOn" else "red",
                "QUIESCING": "blue",
            },
        )

    fields_mapping = {}
    if data and "templateId" in data[0]:
        fields_mapping = {"templateId": "Template", "templateType": "Type"}

    fields_mapping |= {
        "id": "Id",
        "lifecycleStatus": "Status",
        "stale": "Stale",
        "powerState": "Power",
        "agentStatus": "Agent",
        "haiAgentVersion": "Agent Version",
        "sessionPlacementStatus": "Session",
        "vmFreeSessions": "Free Session",
    }
    return util.format_table(data, fields_mapping)


@click.command(name="list")
@click.argument("template-id", type=str, required=False)
@cli.org_id
@common_options.limit
@common_options.sort
@click.option(
    "--cloud",
    "-c",
    type=click.Choice(provider_labels),
    required=False,
    multiple=True,
    help="When template is 'all', filter templates by cloud provider type.",
)
@click.option(
    "--type",
    "-t",
    type=click.Choice(["DEDICATED", "FLOATING", "MULTI_SESSION"]),
    required=False,
    multiple=True,
    help="When template is 'all', filter templates by type.",
)
@click.option(
    "--agent",
    "-a",
    type=click.Choice(["UNAVAILABLE", "ERROR", "AVAILABLE", "INIT", "UNKNOWN", "DOMAIN_ERR", "CUSTOMIZATION_FAILURE"]),
    required=False,
    multiple=True,
    help="Filter VMs by agent status.",
)
@click.option(
    "--power",
    "-p",
    type=click.Choice(["PoweredOn", "PoweredOff", "PoweringOn", "PoweringOff", "Unknown"]),
    required=False,
    multiple=True,
    help="Filter VMs by power state.",
)
@cli.formatter(_format_vm_table)
def list_vms(template_id: str, org: str, cloud: list, type: list, agent: list, power: list, **kwargs):
    """List template VMs"""
    org_id = cli.get_org_id(org)

    vms = []
    if template_id and template_id.lower() == "all":
        templates = admin.template.list(org_id=org_id, limit=200)

        cloud = _to_lower(cloud)
        type = _to_lower(type)

        kwargs["limit"] = 5000
        for t in templates:
            if cloud:
                if t["providerLabel"].lower() not in cloud:
                    continue
            if type:
                if t["templateType"].lower() not in type:
                    continue

            tid = t["id"]
            ret = admin.VM.list(tid, org_id=org_id, **kwargs)
            if ret:
                for v in ret:
                    v["templateId"] = tid
                    v["templateType"] = t["templateType"]
                vms += ret
    else:
        if cloud:
            raise Exception("--cloud parameter is only applicable when template is 'all'.")
        if type:
            raise Exception("--type parameter is only applicable when template is 'all'.")
        template_id = recent.require(template_id, "template")
        ret = admin.VM.list(template_id, org_id=org_id, **kwargs)
        recent.helper.default_list(ret, "vm")

    agent = _to_lower(agent)
    power = _to_lower(power)

    if agent or power:

        def criteria(vm):
            if agent and vm["agentStatus"].lower() not in agent:
                return False
            if power and vm["powerState"].lower() not in power:
                return False
            return True

        vms = list(filter(criteria, vms))
    return vms


def _to_lower(values):
    if values:
        ret = []
        for v in values:
            ret.append(v.lower())
        return ret
