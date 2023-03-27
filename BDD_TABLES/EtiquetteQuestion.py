from HasMany import HasMany
from Pivot import Pivot
from Decorator import decorator


@decorator
class EtiquetteQuestion(Pivot):
    table_name: str = "etiquette_question"

    id: str
    etiquettes: HasMany("etiquettes", "id", "etiquette_id")
    questions: HasMany("questions", "id", "question_id")
