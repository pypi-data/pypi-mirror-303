from .BasicAnalyzer import BasicAnalyzer
from ..utils import nlp_utils


class VdbAnalyzer:

    def __init__(self, basic_analyzer: BasicAnalyzer):
        self.vdb_tokens = []
        self.vdb_fo_tokens = []
        self.vdb_au_tokens = []
        self.vdb_ad_tokens = []

        for lemma in basic_analyzer.lemmas:
            if nlp_utils.is_vdb(lemma):
                self.vdb_tokens.append(lemma)
            if nlp_utils.is_vdb_fo(lemma):
                self.vdb_fo_tokens.append(lemma)
            if nlp_utils.is_vdb_au(lemma):
                self.vdb_au_tokens.append(lemma)
            if nlp_utils.is_vdb_ad(lemma):
                self.vdb_ad_tokens.append(lemma)

        self.n_vdb_tokens = len(self.vdb_tokens)
        self.n_vdb_fo_tokens = len(self.vdb_fo_tokens)
        self.n_vdb_au_tokens = len(self.vdb_au_tokens)
        self.n_vdb_ad_tokens = len(self.vdb_ad_tokens)
