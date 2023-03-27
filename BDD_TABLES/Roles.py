import datetime
from Decorator import decorator

from Table import Table
from ManyToMany import ManyToMany
from BDD_TABLES.RoleUser import RoleUser
from BDD_TABLES.PermissionRole import PermissionRole
from BDD_TABLES.QuestionRole import QuestionRole


@decorator
class Roles(Table):
    id: str
    label: str
    power: str

    created_at: datetime.datetime.timestamp
    updated_at: datetime.datetime.timestamp

    users: ManyToMany("users", RoleUser)
    questions: ManyToMany("questions", QuestionRole)
    permissions: ManyToMany("permissions", PermissionRole)
