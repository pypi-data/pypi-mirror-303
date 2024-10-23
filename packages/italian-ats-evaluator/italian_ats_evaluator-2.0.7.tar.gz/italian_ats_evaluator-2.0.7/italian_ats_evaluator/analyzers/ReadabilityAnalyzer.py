from .BasicAnalyzer import BasicAnalyzer
from .PosAnalyzer import PosAnalyzer


class ReadabilityAnalyzer:

    def __init__(self, basic_analyzer: BasicAnalyzer, pos_analyzer: PosAnalyzer):
        self.ttr = self.__eval_ttr(basic_analyzer)
        self.gulpease = self.__eval_gulpease(basic_analyzer)
        self.flesch_vacca = self.__eval_flesch_vacca(basic_analyzer)
        self.lexical_density = self.__eval_lexical_density(basic_analyzer, pos_analyzer)

    @staticmethod
    def __eval_ttr(basic_analyzer: BasicAnalyzer) -> float:
        return float(basic_analyzer.n_words) / basic_analyzer.n_tokens * 100.0

    @staticmethod
    def __eval_gulpease(basic_analyzer: BasicAnalyzer) -> float:
        return 89 + ((300.0 * basic_analyzer.n_sentences) - (10.0 * basic_analyzer.n_chars)) / float(basic_analyzer.n_tokens)

    @staticmethod
    def __eval_flesch_vacca(basic_analyzer: BasicAnalyzer) -> float:
        return 206 - (0.65 * (basic_analyzer.n_syllables / basic_analyzer.n_tokens) * 100.0) - (
                1.0 * (basic_analyzer.n_tokens / basic_analyzer.n_sentences))

    @staticmethod
    def __eval_lexical_density(basic_analyzer: BasicAnalyzer, pos_analyzer: PosAnalyzer) -> float:
        return (pos_analyzer.n_nouns + pos_analyzer.n_adverbs + pos_analyzer.n_adjectives + pos_analyzer.n_verbs) / float(basic_analyzer.n_tokens)
