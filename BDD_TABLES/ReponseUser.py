from Decorator import decorator

from Table import Table
from HasOne import HasOne


@decorator
class ReponseUser(Table):
    table_name: str = "reponse_user"

    id: str
    body: str
    valide: str
    user_id: str
    session_id: str
    question_id: str

    users: HasOne("users", "user_id")
    sessions: HasOne("sessions", "session_id")
    question: HasOne("questions", "question_id")