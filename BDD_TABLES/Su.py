from HasMany import HasMany
from Pivot import Pivot
from Decorator import decorator


@decorator
class Su(Pivot):
    table_name: str = "su"

    id: str
    session_id: str
    user_id: str

    sessions: HasMany("sessions", "id", "session_id")
    users: HasMany("users", "id", "user_id")
