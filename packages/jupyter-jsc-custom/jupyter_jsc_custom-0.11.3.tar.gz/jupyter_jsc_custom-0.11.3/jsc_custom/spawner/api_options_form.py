import json

from jupyterhub.apihandlers import default_handlers
from jupyterhub.apihandlers.base import APIHandler
from jupyterhub.scopes import needs_scope
from tornado import web

from ..misc import get_custom_config


class SpawnOptionsFormAPIHandler(APIHandler):
    @needs_scope("access:servers")
    async def get(self, user_name, server_name=""):
        user = self.find_user(user_name)
        if user is None:
            # no such user
            self.log.error(
                f"{user_name}:{server_name} - APICall: SpawnOptionsUpdate - No user found",
                extra={"user": user_name, "log_name": f"{user_name}:{server_name}"},
            )
            raise web.HTTPError(404)
        orm_user = user.orm_user

        if server_name not in orm_user.orm_spawners:
            # user has no such server
            self.log.error(
                f"{user_name}:{server_name} - APICall: SpawnOptionsUpdate - No spawner found",
                extra={
                    "user": user,
                    "spawner": server_name,
                    "log_name": f"{user_name}:{server_name}",
                },
            )
            raise web.HTTPError(404)

        auth_state = await user.get_auth_state()
        ret = {}

        # Collect information from Spawner object
        spawner = user.spawners[server_name]
        options_form = auth_state.get("options_form", {})
        try:
            service = spawner.user_options.get(
                "profile", "JupyterLab/JupyterLab"
            ).split("/")[1]
        except:
            spawner.log.exception(
                f"{spawner._log_name} - Could not receive service. Use 3.6 as default"
            )
            service = "3.6"
        system = spawner.user_options.get("system")
        account = spawner.user_options.get("account")
        project = spawner.user_options.get("project")
        interactive_partitions = (
            get_custom_config()
            .get("systems", {})
            .get(system, {})
            .get("interactivePartitions", [])
        )

        # Restructure options form to account+system specific output (defined by spawner.user_options)
        ret = {
            "dropdown_lists": {"projects": [], "partitions": {}, "reservations": {}},
            "resources": {},
        }

        # fill in return dict
        # Skip projects which only have interactive partitions, these are useless for slurm jobs
        projects = []

        # skip all interactive_partitions
        all_projects = (
            options_form.get("dropdown_list", {})
            .get(service, {})
            .get(system, {})
            .get(account, {})
        )
        for project in list(all_projects.keys()):
            batch_partitions = [
                x
                for x in all_projects[project].keys()
                if x not in interactive_partitions
            ]
            if len(batch_partitions) > 0:
                projects.append(project)
                ret["dropdown_lists"]["partitions"][project] = batch_partitions
        ret["dropdown_lists"]["projects"] = projects
        ret["dropdown_lists"]["reservations"] = (
            options_form.get("dropdown_lists", {})
            .get("reservations", {})
            .get(system, {})
            .get(account, {})
        )
        reservations = {}
        for project in projects:
            reservations[project] = {}
            for partition in ret["dropdown_lists"]["partitions"][project]:
                reservations[project][partition] = ["None"] + [
                    x.get("ReservationName")
                    for x in options_form.get("reservations", {}).get(system, [])
                    if (
                        account in x.get("Users", "")
                        or project in x.get("Accounts", "")
                    )
                    and x.get("PartitionName", "(null)") in ["", "(null)", partition]
                    and x.get("State", "INACTIVE") == "ACTIVE"
                ]
        ret["dropdown_lists"]["reservations"] = reservations
        ret["resources"] = (
            options_form.get("resources", {}).get(service, {}).get(system, {})
        )
        self.write(json.dumps(ret))


default_handlers.append(
    (r"/api/users/([^/]+)/server/optionsform", SpawnOptionsFormAPIHandler)
)
default_handlers.append(
    (r"/api/users/([^/]+)/servers/([^/]+)/optionsform", SpawnOptionsFormAPIHandler)
)
