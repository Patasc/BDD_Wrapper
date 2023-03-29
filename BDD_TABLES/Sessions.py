import datetime
from Decorator import decorator
import uuid
import Table as Table
from ManyToMany import ManyToMany
from HasOne import HasOne
from HasMany import HasMany
from BDD_TABLES.Su import Su


@decorator
class Sessions(Table.Table):
    id: str = uuid.uuid4
    sequence_id: str
    code: str

    created_at: datetime.datetime.timestamp = Table.getTime

    users: ManyToMany("users", Su)
    sequence: HasOne("sequences", "sequence_id")
    permissions: HasMany("permissions", "session_id")
    reponses: HasMany("reponse_user", "session_id")
