import uuid
import datetime
import Table
from ManyToMany import ManyToMany
from BDD_TABLES.PermissionRole import PermissionRole
from BDD_TABLES.PermissionUser import PermissionUser


class Permissions(Table.Table):
    id: str = uuid.uuid4
    key: str
    label: str

    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    roles: ManyToMany("roles", PermissionRole)
    users: ManyToMany("users", PermissionUser)
