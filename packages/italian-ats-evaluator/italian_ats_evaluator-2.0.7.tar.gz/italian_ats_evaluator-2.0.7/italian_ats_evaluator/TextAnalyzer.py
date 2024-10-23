from spacy.tokens import Doc

from .analyzers.BasicAnalyzer import BasicAnalyzer
from .analyzers.PosAnalyzer import PosAnalyzer
from .analyzers.ReadabilityAnalyzer import ReadabilityAnalyzer
from .analyzers.VdbAnalyzer import VdbAnalyzer
from .analyzers.VerbsAnalyzer import VerbsAnalyzer
from .utils import nlp_utils


class TextAnalyzer:
    text: str
    text_cleaned: str
    text_processed: Doc

    basic: BasicAnalyzer
    pos: PosAnalyzer
    verbs: VerbsAnalyzer
    vdb: VdbAnalyzer
    readability: ReadabilityAnalyzer

    def __init__(self, text: str, spacy_model_name: str = nlp_utils.DEFAULT_SPACY_MODEL):
        self.text = text
        self.text_cleaned = nlp_utils.clean_text(text)
        self.text_processed = nlp_utils.get_spacy_model(spacy_model_name)(self.text_cleaned)

        self.basic = BasicAnalyzer(self.text_processed)
        self.pos = PosAnalyzer(self.text_processed)
        self.verbs = VerbsAnalyzer(self.text_processed)
        self.vdb = VdbAnalyzer(self.basic)
        self.readability = ReadabilityAnalyzer(self.basic, self.pos)
