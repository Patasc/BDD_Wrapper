from HasMany import HasMany
from Pivot import Pivot
from Decorator import decorator


@decorator
class PermissionUser(Pivot):
    table_name: str = "permission_user"

    id: str
    permission_id: str
    user_id: str

    permissions: HasMany("permissions", "id", "permission_id")
    users: HasMany("users", "id", "user_id")
