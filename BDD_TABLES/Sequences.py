import datetime
from Decorator import decorator

from Table import Table
from ManyToMany import ManyToMany
from HasMany import HasMany
from BDD_TABLES.QuestionSequence import QuestionSequence


@decorator
class Sequences(Table):
    id: str
    label: str

    created_at: datetime.datetime.timestamp
    updated_at: datetime.datetime.timestamp

    sessions: HasMany("sessions", "sequence_id")
    questions: ManyToMany("questions", QuestionSequence)
