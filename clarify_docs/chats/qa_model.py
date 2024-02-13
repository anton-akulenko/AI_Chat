from transformers import AutoTokenizer, pipeline, AutoModelForQuestionAnswering

from .elasticsearch_crud import get_context

MODEL = AutoModelForQuestionAnswering.from_pretrained('henryk/bert-base-multilingual-cased-finetuned-dutch-squad2')
# CONTEXT = 'General relativity is a theory of gravitation developed by Einstein in the years 1907–1915. The development of general relativity began with the equivalence principle, under which the states of accelerated motion and being at rest in a gravitational field (for example, when standing on the surface of the Earth) are physically identical. The upshot of this is that free fall is inertial motion: an object in free fall is falling because that is how objects move when there is no force being exerted on them, instead of this being due to the force of gravity as is the case in classical mechanics. This is incompatible with classical mechanics and special relativity because in those theories inertially moving objects cannot accelerate with respect to each other, but objects in free fall do so. To resolve this difficulty Einstein first proposed that spacetime is curved.'
# CONTEXT="Amsterdam is de hoofdstad en de dichtstbevolkte stad van Nederland."
class QAModel:

    def __init__(self, context_id: str, max_length: int = 1024) -> None:
        self.max_length = max_length
        self.model_name = 'henryk/bert-base-multilingual-cased-finetuned-dutch-squad2'
        self.context = get_context(context_id)

    def tokenize_question(self, question: str, truncation: bool = True, padding: bool = True):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        tokenizer.encode(question, truncation=truncation, padding=padding, max_length=self.max_length)
        return tokenizer

    def create_pipeline(self, tokenizer, model):
        nlp = pipeline('question-answering', model, tokenizer=tokenizer)
        return nlp

    def get_answer(self, question: str, truncation: bool = True, padding: bool = True) -> dict:
        tokenizer = self.tokenize_question(question, truncation, padding)
        model_pipeline = self.create_pipeline(tokenizer, MODEL)
        print(question, self.context)
        answer = model_pipeline(question=question, context=self.context, max_length=self.max_length)
        return answer['answer']
