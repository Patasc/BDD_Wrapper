from HasMany import HasMany
from Pivot import Pivot
from Decorator import decorator


@decorator
class QuestionSequence(Pivot):
    table_name: str = "question_sequence"

    id: str
    question_id: str
    sequence_id: str

    questions: HasMany("questions", "id", "question_id")
    sequences: HasMany("sequences", "id", "sequence_id")
