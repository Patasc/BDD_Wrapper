import uuid
import datetime
from Decorator import decorator

import Table
from ManyToMany import ManyToMany
from HasOne import HasOne
from HasMany import HasMany
from BDD_TABLES.EtiquetteQuestion import EtiquetteQuestion
from BDD_TABLES.QuestionSequence import QuestionSequence
from BDD_TABLES.QuestionRole import QuestionRole


@decorator
class Questions(Table.Table):
    id: str = uuid.uuid4
    label: str
    slug: str
    enonce: str
    type: str
    user_id: str
    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    etiquettes: ManyToMany("etiquettes", EtiquetteQuestion)
    sequences: ManyToMany("sequences", QuestionSequence)
    roles: ManyToMany("roles", QuestionRole)

    user: HasOne("users", "user_id")

    reponses: HasMany("reponses", "question_id")
