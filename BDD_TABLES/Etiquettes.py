import Table
import datetime
from ManyToMany import ManyToMany
from BDD_TABLES.EtiquetteQuestion import EtiquetteQuestion
import uuid


class Etiquettes(Table.Table):
    id: str = uuid.uuid4
    label: str
    color: str
    created_at: datetime.datetime.timestamp = Table.getTime
    updated_at: datetime.datetime.timestamp = Table.getTime

    questions: ManyToMany("questions", EtiquetteQuestion)
