from .TextAnalyzer import TextAnalyzer
from .analyzers.SimilarityAnalyzer import SimilarityAnalyzer
from .analyzers.DiffAnalyzer import DiffAnalyzer
from .utils import nlp_utils


class SimplificationAnalyzer:

    def __init__(self, reference_text: str, simplified_text: str,
                 spacy_model_name: str = nlp_utils.DEFAULT_SPACY_MODEL,
                 sentence_transformers_model_name: str = nlp_utils.DEFAULT_SENTENCE_TRANSFORMERS_MODEL):
        self.reference = TextAnalyzer(reference_text, spacy_model_name)
        self.simplified = TextAnalyzer(simplified_text, spacy_model_name)

        self.similarity = SimilarityAnalyzer(reference_text, simplified_text, sentence_transformers_model_name)
        self.diff = DiffAnalyzer(self.reference.basic, self.simplified.basic)
