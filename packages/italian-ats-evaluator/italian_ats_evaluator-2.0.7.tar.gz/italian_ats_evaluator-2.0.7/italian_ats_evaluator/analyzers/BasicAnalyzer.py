from spacy.tokens import Doc

from ..utils import nlp_utils


class BasicAnalyzer:
    def __init__(self, processed_text: Doc):
        self.tokens = []
        self.tokens_all = []
        self.chars = []
        self.chars_all = []
        self.syllables = []
        self.words = set()
        self.lemmas = []
        self.unique_lemmas = set()
        self.sentences = list(processed_text.sents)

        for token in processed_text:
            self.tokens_all.append(token.text)
            self.chars_all.extend([c for c in token.text])

            if not token.is_punct:
                self.tokens.append(token.text)
                self.chars.extend([c for c in token.text])
                self.syllables.extend(nlp_utils.eval_syllables(token.text))
                self.words.add(token.text)
                self.lemmas.append(token.lemma_)
                self.unique_lemmas.add(token.lemma_)

        self.n_tokens = len(self.tokens)
        self.n_tokens_all = len(self.tokens_all)
        self.n_chars = len(self.chars)
        self.n_chars_all = len(self.chars_all)
        self.n_syllables = len(self.syllables)
        self.n_words = len(self.words)
        self.n_unique_lemmas = len(self.unique_lemmas)
        self.n_sentences = len(self.sentences)
