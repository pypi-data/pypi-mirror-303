from ..utils import nlp_utils
from sentence_transformers import util


class SimilarityAnalyzer:

    def __init__(self, reference_text: str, simplified_text: str, sentence_transformers_model_name: str):
        model = nlp_utils.get_sentence_transformers_model(sentence_transformers_model_name)

        embeddings1 = model.encode([reference_text], convert_to_numpy=True)
        embeddings2 = model.encode([simplified_text], convert_to_numpy=True)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        self.semantic_similarity = float(cosine_scores[0][0]) * 100.0
