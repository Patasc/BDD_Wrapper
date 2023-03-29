import datetime
import uuid

from Decorator import decorator

import Table

from HasOne import HasOne


@decorator
class ApiTokens(Table.Table):
    table_name: str = "api_tokens"

    id: str = uuid.uuid4
    user_id: str
    name: str
    token: str

    created_at: datetime.datetime.timestamp = Table.getTime
    expires_at: datetime.datetime.timestamp = Table.getTime

    users: HasOne("users", "user_id")
