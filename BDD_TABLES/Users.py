import uuid
import datetime

import Table
from Decorator import decorator

from HasMany import HasMany
from ManyToMany import ManyToMany

from BDD_TABLES.RoleUser import RoleUser
from BDD_TABLES.PermissionUser import PermissionUser
from BDD_TABLES.Su import Su


@decorator
class Users(Table.Table):

    table_name = "users"

    id: str = uuid.uuid4
    email: str
    numero: str
    firstname: str
    lastname: str
    password: str

    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    questions: HasMany("questions", "user_id")
    roles: ManyToMany("roles", RoleUser)
    permissions: ManyToMany("permissions", PermissionUser)
    sessions: ManyToMany("sessions", Su)
    tokens: HasMany("api_tokens", "user_id")
    reponses: HasMany("reponse_user", "user_id")
