import datetime
import uuid
from Decorator import decorator

import Table
from ManyToMany import ManyToMany
from HasMany import HasMany
from BDD_TABLES.QuestionSequence import QuestionSequence


@decorator
class Sequences(Table.Table):
    id: str = uuid.uuid4
    label: str

    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    sessions: HasMany("sessions", "sequence_id")
    questions: ManyToMany("questions", QuestionSequence)
