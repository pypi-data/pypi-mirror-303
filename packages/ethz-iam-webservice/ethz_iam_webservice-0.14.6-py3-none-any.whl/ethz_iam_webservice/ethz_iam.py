import json

from .conn import IAMApi
from .group import Group, GroupAlternative
from .mailinglist import Mailinglist
from .person import Guest, Person, PersonLegacy, PersonAlternative
from .user import UserLegacy
from .verbose import VERBOSE


class ETH_IAM:
    def __init__(
        self,
        admin_username=None,
        admin_password=None,
    ):
        self._admin_username = admin_username
        self._admin_password = admin_password
        self.group = Group(admin_username=admin_username, admin_password=admin_password)
        self.new_group = self.group.create
        self.update_group = self.group.update
        self.person_legacy = PersonLegacy(
            admin_username=admin_username, admin_password=admin_password
        )
        self.person = Person(
            admin_username=admin_username, admin_password=admin_password
        )
        self.user_legacy = UserLegacy(
            admin_username=admin_username, admin_password=admin_password
        )
        self.group_alternative = GroupAlternative()
        self.person_alternative = PersonAlternative()
        self.search_groups = self.group_alternative.search_groups
        self.search_persons = self.person_alternative.search_persons
        self.get_person = self.person_legacy.get_person
        self.update_persona = self.person.update_persona
        self.get_persons = self.person_legacy.get_persons
        self.guest = Guest(admin_username=admin_username, admin_password=admin_password)
        self.get_guest = self.guest.get_guest
        self.new_guest = self.guest.create
        self.extend_guest = self.guest.extend
        self.update_guest = self.guest.update
        self.delete_guest = self.guest.delete

    def get_request(self, endpoint, hostname=None, endpoint_base=None):
        resp = self.get_request(
            endpoint=endpoint, hostname=hostname, endpoint_base=endpoint_base
        )
        if resp.ok:
            data = json.loads(resp.content.decode())
            return data
        elif resp.status_code == 401:
            raise ValueError(
                "Provided admin-username/password is incorrect or you are not allowed to do this operation"
            )
        elif resp.status_code == 404:
            raise ValueError("No such user/person/group.")
        else:
            print(resp.status_code)
            try:
                data = json.loads(resp.content.decode())
            except json.decoder.JSONDecodeError as exc:
                raise ValueError(f"received http status: {resp.status_code}") from exc

    def get_user(self, identifier):
        return self.user_legacy.get_user(identifier)

    def del_user(self, identifier, username):
        """Delete a user (persona)"""

        person = self.person.get_person(identifier)
        person.delete_user(username)

    def get_guests_of_lz(self, lz):
        return self.guest.get_guests(host_leitzahl=lz)

    def del_group(self, name):
        """Delete a group and remove it from all its target systems."""
        group = self.group.get_group(name)
        group.delete()

    def get_groups(self, **kwargs):
        """
        agroup=<Admin Group>  -- Get all groups of a given admin group
        name=group_name*      -- all groups starting with «group_name*»
        """
        if kwargs:
            args = "&".join("{}={}".format(key, val) for key, val in kwargs.items())
            endpoint = f"/groups?{args}"
        else:
            raise ValueError("please provide a name or agroup parameter (or both)")
        iam = IAMApi(self._admin_username, self._admin_password)
        data = iam.get_request(endpoint)
        groups = []
        for data_entry in data:
            groups.append(Group.new_from_data(data=data_entry))
        return groups

    def get_group(self, identifier):
        return self.group.get_group(identifier)

    def recertify_group(self, identifier):
        iam = IAMApi(self._admin_username, self._admin_password)
        endpoint = f"/groups/{self.name}/recertify"
        data = iam.put_request(endpoint)
        group = Group.new_from_data(data)
        return group

    def _to_from_group(self, members, action="add", mess="{}"):
        endpoint = f"/groups/{self.name}/members/{action}"
        resp = self.conn.put_request(endpoint, members)
        if resp.ok:
            if VERBOSE:
                print(mess.format(self.name))
            group = Group.new_from_data(resp.json())
            self.replace_field_values(group)
        else:
            data = json.loads(resp.content.decode())
            raise ValueError(data["message"])

    def get_mailinglist(self, identifier=None, **kwargs):
        if identifier:
            endpoint = f"/mailinglists/{identifier}"
        elif kwargs:
            args = "&".join(f"{key}={val}" for key, val in kwargs.items())
            endpoint = f"/mailinglists/?{args}"
        else:
            raise ValueError("please provide an identifier")
        data = self.get_request(endpoint, hostname=self.hostname_new)
        if len(data) > 1:
            raise ValueError(
                f"Identifier {identifier} returned more than one group, it returned {len(data)}."
            )
        return Mailinglist(conn=self, data=data[0])
