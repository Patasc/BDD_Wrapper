import datetime
from Table import Table
from ManyToMany import ManyToMany
from BDD_TABLES.PermissionRole import PermissionRole
from BDD_TABLES.PermissionUser import PermissionUser


class Permissions(Table):
    id: str
    key: str
    label: str

    created_at: datetime.datetime.timestamp
    updated_at: datetime.datetime.timestamp

    roles: ManyToMany("roles", PermissionRole)
    users: ManyToMany("users", PermissionUser)
