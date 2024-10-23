from spacy.tokens import Doc

POS_MAP = {
    "X": "other",
    "NOUN": "nouns",
    "AUX": "verbs",
    "VERB": "verbs",
    "NUM": "number",
    "SYM": "symbols",
    "ADV": "adverbs",
    "DET": "articles",
    "PRON": "pronouns",
    "PART": "particles",
    "ADJ": "adjectives",
    "ADP": "prepositions",
    "PROPN": "proper_nouns",
    "PUNCT": "punctuations",
    "INTJ": "interjections",
    "CCONJ": "coordinating_conjunctions",
    "SCONJ": "subordinating_conjunctions",
}


class PosAnalyzer:
    def __init__(self, processed_text: Doc):
        self.other = []
        self.nouns = []
        self.verbs = []
        self.number = []
        self.symbols = []
        self.adverbs = []
        self.articles = []
        self.pronouns = []
        self.particles = []
        self.adjectives = []
        self.prepositions = []
        self.proper_nouns = []
        self.punctuations = []
        self.interjections = []
        self.coordinating_conjunctions = []
        self.subordinating_conjunctions = []

        for token in processed_text:
            if token.pos_ in POS_MAP:
                getattr(self, POS_MAP[token.pos_]).append(token.text)

        self.n_other = len(self.other)
        self.n_nouns = len(self.nouns)
        self.n_verbs = len(self.verbs)
        self.n_number = len(self.number)
        self.n_symbols = len(self.symbols)
        self.n_adverbs = len(self.adverbs)
        self.n_articles = len(self.articles)
        self.n_pronouns = len(self.pronouns)
        self.n_particles = len(self.particles)
        self.n_adjectives = len(self.adjectives)
        self.n_prepositions = len(self.prepositions)
        self.n_proper_nouns = len(self.proper_nouns)
        self.n_punctuations = len(self.punctuations)
        self.n_interjections = len(self.interjections)
        self.n_coordinating_conjunctions = len(self.coordinating_conjunctions)
        self.n_subordinating_conjunctions = len(self.subordinating_conjunctions)
