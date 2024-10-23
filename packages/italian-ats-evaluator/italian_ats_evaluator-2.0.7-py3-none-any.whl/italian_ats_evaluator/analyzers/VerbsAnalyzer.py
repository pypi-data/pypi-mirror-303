from spacy.tokens import Doc


class VerbsAnalyzer:

    def __init__(self, processed_text: Doc):
        self.active_verbs = []
        self.passive_verbs = []

        for token in processed_text:
            if token.pos_ == "VERB" or token.pos_ == "AUX":
                if token.dep_ == "aux" and "aux:pass" in [c.dep_ for c in token.head.children]:
                    self.passive_verbs.append(token.text)
                elif token.dep_ == "aux:pass" and token.head.pos_ == "VERB":
                    self.passive_verbs.append(token.text)
                elif token.pos_ == "VERB" and "aux:pass" in [c.dep_ for c in token.children]:
                    self.passive_verbs.append(token.text)
                else:
                    self.active_verbs.append(token.text)

        self.n_active_verbs = len(self.active_verbs)
        self.n_passive_verbs = len(self.passive_verbs)
