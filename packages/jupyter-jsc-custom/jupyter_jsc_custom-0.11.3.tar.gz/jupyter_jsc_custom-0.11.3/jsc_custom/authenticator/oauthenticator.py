import asyncio
import copy
import inspect
import json
import os
import re
import time
from datetime import datetime
from urllib.error import HTTPError
from urllib.parse import urlencode

from jupyterhub.utils import new_token
from jupyterhub.utils import url_path_join
from oauthenticator.generic import GenericOAuthenticator
from oauthenticator.oauth2 import OAuthLoginHandler
from oauthenticator.oauth2 import OAuthLogoutHandler
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPClientError
from tornado.httpclient import HTTPRequest
from traitlets import Any
from traitlets import Callable
from traitlets import Dict
from traitlets import Unicode
from traitlets import Union

from ..misc import _custom_config_file
from ..misc import get_custom_config
from ..misc import get_incidents
from ..misc import get_last_incidents_change
from ..misc import get_last_reservation_change
from ..misc import get_reservations

res_pattern = re.compile(
    r"^urn:"
    r"(?P<namespace>.+?(?=:res:)):"
    r"res:"
    r"(?P<systempartition>[^:]+):"
    r"(?P<project>[^:]+):"
    r"act:"
    r"(?P<account>[^:]+):"
    r"(?P<accounttype>[^:]+)$"
)

group_pattern = re.compile(
    r"^urn:"
    r"(?P<namespace>.+?(?=:group:)):"
    r"group:"
    r"(?P<parentgroup>[^:]+)?"
    r"(?::(?!role=)(?P<childgroup>[^:#]+))?"
    r"(?::(?!role=)(?P<grandchildgroup>[^:#]+))?"
    r"(?::role=(?P<role>[^#]+))?"
    r"#(?P<authority>.+)$"
)


async def get_options_form(service, groups, entitlements, preferred_username):
    """
    Create dicts, used by frontend.
     - dropdown_list: contains list for each system/account/project/partition/reservation combination
     - reservations: dict with detailed information about each reservation
     - resources: contains detailed information about each system/partition (no. of nodes, runtime, gpus)

    To allow a different experience for different user groups,
    one can configure overlay configuration in custom_config for each group.
    This enables us to remove/add systems, services, versions for specific groups.
    """
    custom_config = get_custom_config()
    resources = custom_config.get("resources", {})
    default_partitions = custom_config.get("defaultPartitions", {})

    incidents_dict = get_incidents()
    threshold_health = incidents_dict.get("interactive_threshold", 50)
    systems_list = [*custom_config.get("systems", {})]
    incidents_list = [
        x
        for x in systems_list
        if incidents_dict.get(x, {}).get("health", threshold_health - 1)
        >= threshold_health
    ]
    reservations_dict = get_reservations()

    # store used partitions to define, which resources we have to add later on
    partitions_in_use = {}
    options = {}

    # If preferred_username is a seconday
    preferred_username_is_secondary = False
    for entitlement in entitlements:
        match = res_pattern.match(entitlement)
        if match:
            account = match.group("account")
            accounttype = match.group("accounttype")
            if account == preferred_username:
                if accounttype == "secondary":
                    preferred_username_is_secondary = True
                break

    service_config = custom_config.get("services", {}).get(service, {})
    allowed_groups = service_config.get("allowedGroups", [])
    # Check if service is allowed for this user
    if set(groups) >= set(allowed_groups) and allowed_groups:
        # Run through all available Options / Versions
        for option_name, option_config in service_config.get("options", {}).items():
            # Check if option / version is allowed for this user
            allowed_groups = option_config.get("allowedLists", {}).get("groups", [])
            if set(groups) >= set(allowed_groups) and allowed_groups:
                pass
            else:
                # Skip this option
                continue

            # First let's add some hpc systems
            for entitlement in entitlements:
                match = res_pattern.match(entitlement)
                if match:
                    systempartition = match.group("systempartition").lower()
                    system = custom_config.get("mapSystems", {}).get(
                        systempartition, None
                    )
                    partition = custom_config.get("mapPartitions", {}).get(
                        systempartition, None
                    )
                    project = match.group("project")
                    account = match.group("account")
                    accounttype = match.group("accounttype")

                    if not system or not partition:
                        continue

                    if system in incidents_list:
                        continue

                    if (
                        preferred_username_is_secondary
                        and account != preferred_username
                    ):
                        # If preferred username is of type secondary, only add the preferred one
                        continue

                    if system not in option_config.get("allowedLists", {}).get(
                        "systems", []
                    ):
                        # Must be supported by the service option
                        continue

                    if system not in custom_config.get("systems", {}).keys():
                        # If it's not configured, we don't have to add it
                        continue

                    if option_name not in options.keys():
                        options[option_name] = {}
                    if system not in options[option_name].keys():
                        options[option_name][system] = {}
                    if account not in options[option_name][system].keys():
                        options[option_name][system][account] = {}
                    if project not in options[option_name][system][account].keys():
                        options[option_name][system][account][project] = {}
                        for interactive_partition in (
                            custom_config.get("systems", {})
                            .get(system, {})
                            .get("interactivePartitions", [])
                        ):
                            options[option_name][system][account][project][
                                interactive_partition
                            ] = {}
                    if (
                        partition
                        not in options[option_name][system][account][project].keys()
                    ):
                        options[option_name][system][account][project][partition] = {}

                    if system not in partitions_in_use.keys():
                        partitions_in_use[system] = []
                        for interactive_partition in (
                            custom_config.get("systems", {})
                            .get(system, {})
                            .get("interactivePartitions", [])
                        ):
                            partitions_in_use[system].append(interactive_partition)

                    if partition not in partitions_in_use[system]:
                        partitions_in_use[system].append(partition)

                    # Add default partitions
                    for value in default_partitions.get(systempartition, []):
                        new_partition = custom_config.get("mapPartitions", {}).get(
                            value, value
                        )
                        if (
                            new_partition
                            not in options[option_name][system][account][project].keys()
                        ):
                            partitions_in_use[system].append(new_partition)
                            options[option_name][system][account][project][
                                new_partition
                            ] = ["None"] + sorted(
                                [
                                    x
                                    for x in reservations_dict.get(system, [])
                                    if (
                                        (
                                            project in x.get("Accounts", "").split(",")
                                            or account in x.get("Users", "").split(",")
                                        )
                                        and (
                                            (not x.get("PartitionName", ""))
                                            or partition
                                            in x.get("PartitionName", "").split(",")
                                        )
                                    )
                                ],
                                key=lambda x: x["ReservationName"],
                            )

                    options[option_name][system][account][project][partition] = [
                        "None"
                    ] + sorted(
                        [
                            x
                            for x in reservations_dict.get(system, [])
                            if (
                                (
                                    project in x.get("Accounts", "").split(",")
                                    or account in x.get("Users", "").split(",")
                                )
                                and (
                                    (not x.get("PartitionName", ""))
                                    or partition
                                    in x.get("PartitionName", "").split(",")
                                )
                            )
                        ],
                        key=lambda x: x["ReservationName"],
                    )

            # Now add all non-hpc systems
            for system in option_config.get("allowedLists", {}).get("systems", []):
                if system not in custom_config.get("systems", {}).keys():
                    # If it's not configured, we don't have to add it
                    continue

                if system in incidents_list:
                    continue

                # if not HPC system: add it
                backend_service = (
                    custom_config.get("systems", {})
                    .get(system, {})
                    .get("backendService")
                )
                if (
                    custom_config.get("backendServices", {})
                    .get(backend_service, {})
                    .get("type", "")
                    != "unicore"
                ):
                    if option_name not in options.keys():
                        options[option_name] = {}
                    if system not in options[option_name].keys():
                        options[option_name][system] = {}

    if not options:
        return {
            "message": f"You're not allowed to use {service}. Please contact support if you think that's not correct.",
            "dropdown_list": {},
            "resources": {},
            "reservations": {},
        }

    resources_replaced = {
        option: {
            system: {
                partition: resources[system][partition]
                for partition in partitions_in_use.get(system, [])
            }
            for system in _systems.keys()
        }
        for option, _systems in options.items()
    }

    return {
        "dropdown_list": options,
        "reservations": reservations_dict,
        "resources": resources_replaced,
    }


class VoException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def get_groups_default(user_info):
    """
    Return all groups a user is part of
    JSC Login uses eduPersonEntitlement for group memberships.
    Definition is listed here:
     - https://zenodo.org/record/6533400/files/AARC-G069%20Guidelines%20for%20expressing%20group%20membership%20and%20role%20information.pdf

    All users are also in the default group

    Example:
        urn:<namespace>:group:parentgroup:childgroup:grandchildgroup:role=somerole#authority

    User will be in 4 groups:
        -   urn:<namespace>:group:parentgroup:childgroup:grandchildgroup
        -   urn:<namespace>:group:parentgroup:childgroup:grandchildgroup:role=somerole
        -   urn:<namespace>:group:parentgroup:childgroup:grandchildgroup:role=somerole#authority
        -   urn:<namespace>:group:parentgroup:childgroup:grandchildgroup#authority
        -   urn:<namespace>:group:parentgroup:childgroup
        -   urn:<namespace>:group:parentgroup:childgroup#authority
        -   urn:<namespace>:group:parentgroup
        -   urn:<namespace>:group:parentgroup#authority
        -   default
    """
    entitlements = user_info.get("entitlements", [])
    groups = []

    def add_sub_groups(group, role, authority, rightmost_group=True):
        if role and rightmost_group:
            group_role = f"{group}:role={role}"
            if group_role not in groups:
                groups.append(group_role)
        if authority:
            group_authority = f"{group}#{authority}"
            if group_authority not in groups:
                groups.append(group_authority)
        if role and rightmost_group and authority:
            group_role_authority = f"{group}:role={role}#{authority}"
            if group_role_authority not in groups:
                groups.append(group_role_authority)

    for entry in entitlements:
        match = group_pattern.match(entry)
        if match:
            namespace = match.group("namespace")
            grandchildgroup = match.group("grandchildgroup")
            childgroup = match.group("childgroup")
            parentgroup = match.group("parentgroup")
            role = match.group("role")
            authority = match.group("authority")
            rightmost_group = True
            if grandchildgroup:
                group = f"urn:{namespace}:group:{parentgroup}:{childgroup}:{grandchildgroup}"
                if group not in groups:
                    groups.append(group)
                add_sub_groups(group, role, authority, rightmost_group)
                rightmost_group = False
            if childgroup:
                group = f"{namespace}:{parentgroup}:{childgroup}"
                if group not in groups:
                    groups.append(group)
                add_sub_groups(group, role, authority, rightmost_group)
                rightmost_group = False
            if parentgroup:
                group = f"{namespace}:{parentgroup}"
                if group not in groups:
                    groups.append(group)
                add_sub_groups(group, role, authority, rightmost_group)
                rightmost_group = False

    if "default" not in groups:
        groups.append("default")
    return list(set(groups))


def get_services(auth_state, custom_config):
    ## We want to be able to offer multiple service types.
    ## We use all services listed in custom_config.services
    services_available = []
    service_active = ""
    user_groups = auth_state["groups"]

    for service_name, service_config in custom_config.get("services", {}).items():
        allowed_groups = service_config.get("allowedGroups", [])
        if set(user_groups) >= set(allowed_groups) and allowed_groups:
            services_available.append(service_name)
            # User is allowed to use this service

    if services_available:
        # sort them by weight
        services_weight = [
            (x, custom_config.get("services", {}).get(x, {}).get("weight", 99))
            for x in services_available
        ]
        services_weight.sort(key=lambda x: x[1])
        if services_weight:
            # and use the first service by weight
            service_active = services_available[0]
        else:
            # if no services are defined in the specific groups, we just use JupyterLab.
            service_active = "JupyterLab"
    return service_active, services_available


class CustomLogoutHandler(OAuthLogoutHandler):
    """
    Default JupyterHub logout mechanism is a bit limited.
    This class allows us to do the followings (optional):
        - logout on all devices (by creating a new cookie_id)
        - stop all running services

    Both options can be triggered by url arguments
        - ?alldevices=true&stopall=true

    Next to this optional features, it also handles the oauth tokens.
    It always revokes the current access tokens.
    It revokes the refresh token if both conditions are true:
        - user logs out from all devices
        - stops all running services, or has none running

    """

    async def handle_logout(self):
        user = self.current_user
        if not user:
            self.log.debug("Could not retrieve current user for logout call.")
            return

        all_devices = self.get_argument("alldevices", "false").lower() == "true"
        stop_all = self.get_argument("stopall", "false").lower() == "true"
        # Stop all servers before revoking tokens
        if stop_all:
            await self._shutdown_servers(user)

        if user.authenticator.enable_auth_state:
            tokens = {}
            auth_state = await user.get_auth_state()
            access_token = auth_state.get("access_token", None)
            if access_token:
                tokens["access_token"] = access_token
                auth_state["access_token"] = None
                auth_state["exp"] = "0"
            # Only revoke refresh token if we logout from all devices and stop all services
            if all_devices and (stop_all or not user.active):
                refresh_token = auth_state.get("refresh_token", None)
                if refresh_token:
                    tokens["refresh_token"] = refresh_token
                    auth_state["refresh_token"] = None

            unity_revoke_url = url_path_join(
                user.authenticator.token_url.rstrip("/token"), "revoke"
            )
            client_id = user.authenticator.client_id
            unity_revoke_config = get_custom_config().get("unity", {}).get("revoke", {})
            unity_revoke_request_kwargs = unity_revoke_config.get(
                "requestKwargs", {"request_timeout": 10}
            )

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = {"client_id": client_id, "logout": "true"}

            log_extras = {
                "unity_revoke_url": unity_revoke_url,
                "unity_revoke_request_kwargs": unity_revoke_request_kwargs,
                "data": copy.deepcopy(data),
            }

            for key, value in tokens.items():
                data["token_type_hint"] = key
                data["token"] = value
                log_extras["data"]["token_type_hint"] = key
                log_extras["data"]["token"] = "***"
                try:
                    req = HTTPRequest(
                        f"{unity_revoke_url}",
                        method="POST",
                        headers=headers,
                        body=urlencode(data),
                        **unity_revoke_request_kwargs,
                    )
                    resp = await user.authenticator.fetch(req)
                    if resp and resp.error:
                        raise Exception(
                            f"Received unexpected status code: {resp.code}: {resp.error}"
                        )
                except (HTTPError, HTTPClientError):
                    self.log.critical(
                        f"{user.name} - Could not revoke token",
                        extra=log_extras,
                        exc_info=True,
                    )
                except:
                    self.log.critical(
                        f"{user.name} - Could not revoke token.",
                        extra=log_extras,
                        exc_info=True,
                    )
                else:
                    self.log.debug(
                        f"{user.name} - Unity revoke {key} call successful.",
                        extra=log_extras,
                    )
            await user.save_auth_state(auth_state)

        # Set new cookie_id to invalidate previous cookies
        if all_devices:
            orm_user = user.orm_user
            orm_user.cookie_id = new_token()
            self.db.commit()

    async def get(self):
        await self.handle_logout()
        await self.default_handle_logout()
        path = self.get_argument("next", default=False)
        if path:
            self.redirect(url_path_join(self.hub.base_url, path), permanent=False)
        else:
            await self.render_logout_page()


class CustomLoginHandler(OAuthLoginHandler):
    """
    This LoginHandler adds a small feature to the default OAuthLoginHandler:

    - send url parameters to the oauth endpoint.

    Enables us to select the preselected Authenticator in Unity.
    For safety reasons, one has to configure the allowed "extra_params".

    Example::
        def extra_params(handler):
            return {
                "key": ["allowed1", "allowed2"]
            }
        c.Authenticator.extra_params_allowed_runtime = extra_params
    """

    def authorize_redirect(self, *args, **kwargs):
        extra_params = kwargs.setdefault("extra_params", {})
        if self.authenticator.extra_params_allowed_runtime:
            if callable(self.authenticator.extra_params_allowed_runtime):
                extra_params_allowed = self.authenticator.extra_params_allowed_runtime()
            else:
                extra_params_allowed = self.authenticator.extra_params_allowed_runtime
            extra_params.update(
                {
                    k[len("extra_param_") :]: "&".join([x.decode("utf-8") for x in v])
                    for k, v in self.request.arguments.items()
                    if k.startswith("extra_param_")
                    and set([x.decode("utf-8") for x in v]).issubset(
                        extra_params_allowed.get(k[len("extra_param_") :], [])
                    )
                }
            )
        return super().authorize_redirect(*args, **kwargs)


class CustomGenericOAuthenticator(GenericOAuthenticator):
    """
    This Authenticator offers additional information in the user's auth_state.
    That's necessary for Jupyter at JSC, because we need the options_form and
    some other tools at the /hub/home site to skip the "Select Options" site.
    """

    login_handler = CustomLoginHandler
    logout_handler = CustomLogoutHandler

    tokeninfo_url = Unicode(
        config=True,
        help="""The url retrieving information about the access token""",
    )

    extra_params_allowed_runtime = Union(
        [Dict(), Callable()],
        config=True,
        help="""Allowed extra GET params to send along with the initial OAuth request
        to the OAuth provider.
        Usage: GET to localhost:8000/hub/oauth_login?extra_param_<key>=<value>
        This argument defines the allowed keys and values.
        Example:
        ```
        {
            "key": ["value1", "value2"],
        }
        ```
        All accepted extra params will be forwarded without the `extra_param_` prefix.
        """,
    )

    outpost_flavors_auth = Any(
        help="""
        An optional hook function you can implement to define the body
        send to the JupyterHub Outpost, when pulling user specific
        flavors. The value returned by this function, can be used by the
        JupyterHub Outpost to define user specific flavors.
        
        Only used if user specific flavors are configured for a system.
        
        This may be a coroutine.
        
        Example::
        
            async def outpost_flavors_auth(system_name, authentication_safe):
                ret = {
                    "access_token": authentication_safe["auth_state"].get("access_token", ""),
                    "name": authentication_safe["auth_state"].get("name", ""),
                    "groups": authentication_safe["auth_state"].get("groups", []),
                }
                return ret
            
            c.OutpostSpawner.outpost_flavors_auth = outpost_flavors_auth
        """,
        default_value=False,
    ).tag(config=True)

    def get_user_groups(self, user_info):
        return list(super().get_user_groups(user_info))

    claim_groups_key = Any(
        default_value=get_groups_default,
        help="""
        Userdata groups claim key from returned json for USERDATA_URL.

        Can be a string key name (use periods for nested keys), or a callable
        that accepts the returned json (as a dict) and returns the groups list.

        This configures how group membership in the upstream provider is determined
        for use by `allowed_groups`, `admin_groups`, etc. If `manage_groups` is True,
        this will also determine users' _JupyterHub_ group membership.
        """,
    ).tag(config=True)

    # Refresh "auth" at every call. This will actually check if there's an
    # update for reservations/incidents/custom_config.
    # true_auth_refresh_age will be used as interval to check if
    # the oauth token must be refreshed
    true_auth_refresh_age = 300

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.true_auth_refresh_age = self.auth_refresh_age
        self.auth_refresh_age = 1

    def get_callback_url(self, handler=None):
        # Replace _host_ in callback_url with current request
        # Allows us to support multiple hostnames and redirect
        # to the used one.
        ret = super().get_callback_url(handler)
        if self.oauth_callback_url and handler and "_host_" in ret:
            ret = ret.replace("_host_", handler.request.host)
        return ret

    async def update_auth_state_custom_config(self, authentication, force=False):
        update_authentication = False
        try:
            last_change_custom_config = os.path.getmtime(_custom_config_file)
        except:
            last_change_custom_config = 0

        if (
            force
            or authentication["auth_state"].get("custom_config_update", 0)
            < last_change_custom_config
            or authentication["auth_state"].get("incidents_update", 0)
            < get_last_incidents_change()
        ):
            """
            If there's a new incident or the custom config file has changed,
            we have to renew the hpc accounts and add the new custom_config
            file to the auth_state, which is forwarded to the frontend.
            """
            custom_config = get_custom_config()
            authentication["auth_state"][
                "custom_config_update"
            ] = last_change_custom_config
            authentication["auth_state"][
                "incidents_update"
            ] = get_last_incidents_change()
            authentication["auth_state"][
                "reservation_update"
            ] = get_last_reservation_change()

            # Custom config update may have changed the resources we want to offer
            authentication["auth_state"]["groups"] = self.get_user_groups(
                authentication["auth_state"][self.user_auth_state_key]
            )
            service_active, services_available = get_services(
                authentication["auth_state"], custom_config
            )
            authentication["auth_state"]["service_active"] = service_active
            authentication["auth_state"]["services_available"] = services_available
            authentication["auth_state"]["options_form"] = await get_options_form(
                service=authentication["auth_state"]["service_active"],
                groups=authentication["auth_state"]["groups"],
                entitlements=authentication["auth_state"]["entitlements"],
                preferred_username=authentication["auth_state"]["preferred_username"],
            )
            update_authentication = True
        if (
            authentication["auth_state"].get("reservation_update", 0)
            < get_last_reservation_change()
        ):
            authentication["auth_state"]["options_form"] = await get_options_form(
                service=authentication["auth_state"]["service_active"],
                groups=authentication["auth_state"]["groups"],
                entitlements=authentication["auth_state"]["entitlements"],
                preferred_username=authentication["auth_state"]["preferred_username"],
            )
            authentication["auth_state"][
                "reservation_update"
            ] = get_last_reservation_change()
            update_authentication = True
        if update_authentication:
            return authentication
        else:
            return True

    def user_info_to_username(self, user_info):
        username = super().user_info_to_username(user_info)
        normalized_username = self.normalize_username(username)
        self.log.info(
            f"Login {normalized_username} - Received username from user_info: {user_info}"
        )
        return username

    async def refresh_user(self, user, handler=None):
        # We use refresh_user to update auth_state, even if
        # the access token is not outdated yet.
        auth_state = await user.get_auth_state()
        if not auth_state:
            return False
        authentication = {"auth_state": auth_state}
        threshold = 2 * self.true_auth_refresh_age
        now = time.time()
        rest_time = int(auth_state.get("exp", now)) - now
        if threshold > rest_time:
            ## New access token required
            try:
                refresh_token_save = auth_state.get("refresh_token", None)
                self.log.debug(
                    f"{user.name} - Refresh authentication. Rest time: {rest_time}"
                )
                if not refresh_token_save:
                    self.log.debug(
                        f"{user.name} - Auth state has no refresh token. Return False."
                    )
                    return False
                params = {
                    "refresh_token": auth_state.get("refresh_token"),
                    "grant_type": "refresh_token",
                    "scope": " ".join(self.scope),
                }

                token_info = await self.get_token_info(handler, params)
                # use the access_token to get userdata info
                user_info = await self.token_to_user(token_info)
                # extract the username out of the user_info dict and normalize it
                username = self.user_info_to_username(user_info)
                username = self.normalize_username(username)

                authentication["name"] = username
                if not token_info.get("refresh_token", None):
                    token_info["refresh_token"] = refresh_token_save

                authentication["auth_state"] = self.build_auth_state_dict(
                    token_info, user_info
                )
                ret = await self.run_post_auth_hook(handler, authentication)
            except:
                self.log.exception(f"{user.name} - Refresh of access token failed")
                ret = False
        else:
            # Update custom config, if neccessary
            try:
                ret = await self.update_auth_state_custom_config(authentication)
            except:
                self.log.exception(
                    f"{user.name} - Could not update user auth_state, log out"
                )
                ret = False
        return ret

    async def run_outpost_flavors_auth(self, system_name, authentication_safe):
        if self.outpost_flavors_auth:
            ret = self.outpost_flavors_auth(system_name, authentication_safe)
            if inspect.isawaitable(ret):
                ret = await ret
        else:
            ret = {
                "access_token": authentication_safe["auth_state"].get(
                    "access_token", ""
                ),
                "name": authentication_safe["auth_state"].get("name", ""),
                "groups": authentication_safe["auth_state"].get("groups", []),
            }
        return ret

    async def post_auth_hook(self, authenticator, handler, authentication):
        # After the user was authenticated we collect additional information
        #  - expiration of access token (so we can renew it before it expires)
        #  - last login (additional information for the user)
        #  - used authenticator (to classify user)
        #  - hpc_list (allowed systems, projects, partitions, etc.)
        access_token = authentication["auth_state"]["access_token"]
        headers = {
            "Accept": "application/json",
            "User-Agent": "JupyterHub",
            "Authorization": f"Bearer {access_token}",
        }
        req = HTTPRequest(self.tokeninfo_url, method="GET", headers=headers)
        try:
            resp = await authenticator.fetch(req)
        except HTTPClientError as e:
            authenticator.log.warning(
                "{name} - Could not request user information - {e}".format(
                    name=authentication.get("name", "unknownName"), e=e
                )
            )
            raise Exception(e)
        authentication["auth_state"]["exp"] = resp.get("exp")
        authentication["auth_state"]["last_login"] = datetime.now().strftime(
            "%H:%M:%S %Y-%m-%d"
        )

        preferred_username = (
            authentication["auth_state"]
            .get(self.user_auth_state_key, {})
            .get("preferred_username", None)
        )
        authentication["auth_state"]["preferred_username"] = preferred_username
        authentication["auth_state"]["entitlements"] = (
            authentication.get("auth_state", {})
            .get(self.user_auth_state_key, {})
            .get("entitlements", [])
        )
        handler.statsd.incr(f"login.preferred_username.{preferred_username}")

        authentication["auth_state"]["name"] = authentication["name"]
        # In this part we classify the user in specific groups.
        try:
            authentication["auth_state"]["groups"] = self.get_user_groups(
                authentication["auth_state"][self.user_auth_state_key]
            )
        except VoException as e:
            self.log.warning(
                "{name} - Could not get groups for user - {e}".format(
                    name=authentication.get("name", "unknownName"), e=e
                )
            )
            raise e

        try:
            user_specific_flavors = await self.collect_flavors_from_outposts(
                authentication
            )
            if user_specific_flavors:
                self.log.info(
                    "{name} post auth hook - add specific flavors".format(
                        name=authentication["auth_state"].get("name", "unknownName")
                    )
                )
                authentication["auth_state"]["outpost_flavors"] = user_specific_flavors
        except:
            self.log.exception(
                "Could not check user specific flavors. Use default flavors"
            )

        # Now we collect the hpc information and create a useful python dict from it
        ## First let's add some "default_partitions", that should be added to each user,
        ## even if it's not listed in hpc information
        custom_config = get_custom_config()

        service_active, services_available = get_services(
            authentication["auth_state"], custom_config
        )
        authentication["auth_state"]["service_active"] = service_active
        authentication["auth_state"]["services_available"] = services_available

        ## With this list we can now create the spawner.options_form value.
        ## We will store this in the auth_state instead of the Spawner:
        ##
        ## - We want to skip the spawn.html ("Server Options") page. The user should
        ##   configure the JupyterLab on /hub/home and we redirect directly to spawn_pending.
        ##   Spawner.get_options_fform is an async function, so we cannot call it in Jinja.
        ##   We will start Spawner Objects via query_options/form_options, so no need for user_options
        ##   in the SpawnerClass.
        ##

        authentication["auth_state"][
            "reservation_update"
        ] = get_last_reservation_change()
        authentication["auth_state"]["options_form"] = await get_options_form(
            service=authentication["auth_state"]["service_active"],
            groups=authentication["auth_state"]["groups"],
            entitlements=authentication["auth_state"]["entitlements"],
            preferred_username=authentication["auth_state"]["preferred_username"],
        )

        ## We have a few custom config features on the frontend. For this, we have to store
        ## (parts of) the custom_config in the user's auth state
        authentication = await self.update_auth_state_custom_config(
            authentication, force=True
        )

        return authentication

    async def collect_flavors_from_outposts(self, authentication):
        custom_config = get_custom_config()

        # Systems can have the option "userflavors": true.
        # If that's the case we will send a request to the outpost, to
        # receive the allowed flavors for this specific user

        ret = {}
        tasks = []
        http_client = AsyncHTTPClient(
            force_instance=True, defaults=dict(validate_cert=False)
        )
        system_names = []
        for system_name, system_config in custom_config.get("systems", {}).items():
            backend_service = system_config.get("backendService", None)
            if not backend_service:
                self.log.warning(
                    f"BackendService for {system_name} not configured. Skip"
                )
                continue
            service_config = custom_config.get("backendServices", {}).get(
                backend_service, {}
            )
            if service_config.get("userflavors", False):
                services_url = service_config.get("urls", {}).get("services", None)
                if services_url:
                    url = services_url[: -len("services")] + "userflavors"
                else:
                    self.log.warning(
                        f"OutpostFlavors user specific - service url not defined. Skip {system_name}"
                    )
                    continue

                authentication_safe = copy.deepcopy(authentication)
                if "refresh_token" in authentication_safe.get("auth_state", {}).keys():
                    del authentication_safe["auth_state"]["refresh_token"]
                if "refresh_token" in authentication_safe.keys():
                    del authentication_safe["refresh_token"]
                authentication_used = await self.run_outpost_flavors_auth(
                    system_name, authentication_safe
                )
                self.log.info(
                    f"OutpostFlavors user specific - Retrieve flavors from {system_name} / {url}"
                )
                auth = os.environ.get(f"AUTH_{backend_service.upper()}")
                headers = {
                    "Authorization": f"Basic {auth}",
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                }
                request_kwargs = service_config.get(
                    "userflavorsRequestKwargs", {"request_timeout": 10}
                )
                req = HTTPRequest(
                    url,
                    method="POST",
                    headers=headers,
                    body=json.dumps(authentication_used),
                    **request_kwargs,
                )
                tasks.append(http_client.fetch(req, raise_error=False))
                system_names.append(system_name)
        results = await asyncio.gather(*tasks, return_exceptions=True)
        names_results = list(zip(system_names, results))
        for name_result in names_results:
            try:
                if name_result[1].code == 200:
                    self.log.info(
                        f"OutpostFlavors user specific - {name_result[0]} successful"
                    )
                    result_json = json.loads(name_result[1].body)
                    ret[name_result[0]] = result_json
                else:
                    self.log.warning(
                        f"OutpostFlavors user specific - {name_result[0]} - Answered with {name_result[1].code} ({name_result[1]})"
                    )
            except:
                self.log.exception(
                    f"OutpostFlavors user specific - {name_result.get(0, 'unknown')} Could not load result into json"
                )
        return ret
