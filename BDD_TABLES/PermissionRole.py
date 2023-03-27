from HasMany import HasMany
from Pivot import Pivot
from Decorator import decorator


@decorator
class PermissionRole(Pivot):
    table_name: str = "permission_role"

    id: str
    permission_id: str
    role_id: str

    permissions: HasMany("permissions", "id", "permission_id")
    roles: HasMany("roles", "id", "role_id")
