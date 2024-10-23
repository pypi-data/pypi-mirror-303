import json
from dataclasses import asdict, dataclass, field
from typing import List

from .conn import IAMApiLegacy
from .person import PersonLegacy
from .service import Mailbox, Service
from .utils import to_date
from .verbose import VERBOSE

service_map = {
    "LDAP": "LDAP",
    "LDAPS": "LDAP",
    "MAILBOX": "Mailbox",
    "AD": "AD",
    "ACTIVE DIRECTORY": "AD",
    "VPN": "WLAN_VPN",
    "WLAN_VPN": "WLAN_VPN",
}

map_iamlegacyfields2internal = {
    "username": "username",
    "sn": "sn",
    "givenName": "givenName",
    "nuid": "nuid",
    "npid": "npid",
    "uidNumber": "uidNumber",
    "gidNumber": "gidNumber",
    "home_directory": "home_directory",
    "memo": "description",
    "login_shell": "login_shell",
    "cre_date": "cre_date",
    "cre_by": "cre_by",
    "mod_date": "mod_date",
    "mod_by": "mod_by",
    "valid_until": "valid_until",
    "services": "services",
}


@dataclass
class UserLegacy(IAMApiLegacy):
    username: str = None
    sn: str = None
    givenName: str = None
    npid: int = None
    nuid: int = None
    uidNumber: int = None
    gidNumber: int = None
    cre_date: str = None
    cre_by: str = None
    mod_date: str = None
    mod_by: str = None
    valid_until: str = None
    home_directory: str = None
    services: list[dict] = field(default_factory=list)
    description: str = None
    login_shell: str = None

    @property
    def data(self):
        return asdict(self)

    def delete(self):
        endpoint = f"usermgr/person/{self.username}"
        resp = self.delete_request(endpoint)
        if resp.ok:
            if VERBOSE:
                print(f"User {self.username} deleted.")
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data["message"])

    def new_from_data(self, data):
        new_user = {}
        for data_field in data:
            if data_field.lower() in map_iamlegacyfields2internal:
                new_user[map_iamlegacyfields2internal[data_field.lower()]] = data[
                    data_field
                ]
            else:
                pass

        for service in new_user.get("services", []):
            service["login_until"] = to_date(service["login_until"]).strftime(
                "%Y-%m-%d"
            )
            service["delete_after"] = to_date(service["delete_after"]).strftime(
                "%Y-%m-%d"
            )

        user = UserLegacy(**new_user)
        user._admin_username = self._admin_username
        user._admin_password = self._admin_password
        return user

    def get_user(self, identifier):
        endpoint = f"usermgr/user/{identifier}"
        data = self.get_request(endpoint)
        return self.new_from_data(data)

    def get_person(self):
        endpoint = f"usermgr/person/{self.npid}"
        data = self.get_request(endpoint)
        return PersonLegacy(data=data)

    def _to_from_group(self, group_name, action="add", mess="{} {}"):
        endpoint = f"/groups/{group_name}/members/{action}"
        body = [self.username]
        self.put_request(endpoint, body)
        if VERBOSE:
            print(mess.format(self.username, group_name))

    def add_to_group(self, group_name):
        self._to_from_group(
            group_name, action="add_forgiving", mess="Added user {} to group {}"
        )

    def remove_from_group(self, group_name):
        self._to_from_group(group_name, "del", mess="Removed user {} from group {}")

    def grant_service(self, service_name) -> List:
        if service_name.upper() in service_map:
            service_name = service_map[service_name.upper()]
        endpoint = f"usermgr/user/{self.username}/service/{service_name}"
        info = self.post_request(endpoint, {})
        return info

    def revoke_service(self, service_name):
        if service_name.upper() in service_map:
            service_name = service_map[service_name.upper()]
        endpoint = "usermgr/user/{}/service/{}".format(self.username, service_name)
        resp = self.delete_request(endpoint)
        if resp.ok:
            if VERBOSE:
                print("Service {} revoked from {}".format(service_name, self.username))
        elif resp.status_code == 401:
            raise ValueError(
                "Provided admin-username/password is incorrect or you are not allowed to do this operation"
            )
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data["message"])

    def get_service(self, service_name):
        clean_service_name = service_map.get(service_name.upper())
        if not clean_service_name:
            raise ValueError(f"No such service: {service_name}")
        service_name = clean_service_name
        endpoint = "usermgr/user/{}/service/{}".format(self.username, service_name)
        resp = self.get_request(endpoint)
        data = json.loads(resp.content.decode())
        if resp.ok:
            if service_name == "Mailbox":
                return Mailbox(
                    username=self.username,
                    service_name=service_name,
                    data=data,
                )
            else:
                return Service(
                    username=self.username,
                    service_name=service_name,
                    data=data,
                )
        elif resp.status_code == 401:
            raise ValueError(
                "Provided admin-username/password is incorrect or you are not allowed to do this operation"
            )
        else:
            raise ValueError(data["message"])

    def set_password(self, password, service_name="LDAPS"):
        """Sets a password for a given service"""

        if service_name.upper() not in service_map:
            raise ValueError(f"Cannot set password for service: {service_name}. Sorry!")

        endpoint = f"usermgr/user/{self.username}/service/{service_map[service_name.upper()]}/password"
        body = {"password": password}
        self.put_request(endpoint, body)
