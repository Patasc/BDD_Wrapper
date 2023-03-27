import datetime
from Decorator import decorator

from Table import Table
from ManyToMany import ManyToMany
from HasOne import HasOne
from HasMany import HasMany
from BDD_TABLES.Su import Su


@decorator
class Sessions(Table):
    id: str
    sequence_id: str
    code: str

    created_at: datetime.datetime.timestamp

    users: ManyToMany("users", Su)
    sequence: HasOne("sequences", "sequence_id")
    permissions: HasMany("permissions", "session_id")
    reponses: HasMany("reponse_user", "session_id")
