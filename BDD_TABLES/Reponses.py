import uuid
import datetime
from Decorator import decorator

import Table
from HasOne import HasOne


@decorator
class Reponses(Table.Table):
    id: str = uuid.uuid4
    body: str
    valide: str
    question_id: str

    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    questions: HasOne("questions", "question_id")
