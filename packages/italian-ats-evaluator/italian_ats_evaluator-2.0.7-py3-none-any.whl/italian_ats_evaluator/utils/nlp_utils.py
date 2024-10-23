import spacy
import pyphen
import pkgutil
from sentence_transformers import SentenceTransformer

DEFAULT_SPACY_MODEL = "it_core_news_lg"
DEFAULT_SENTENCE_TRANSFORMERS_MODEL = "intfloat/multilingual-e5-base"

dic = pyphen.Pyphen(lang='it')

italian_vdb_fo = {a for a in pkgutil.get_data('italian_ats_evaluator', 'nvdb/FO.txt').decode('utf-8').replace('\r', '').split('\n')}
italian_vdb_au = {a for a in pkgutil.get_data('italian_ats_evaluator', 'nvdb/AU.txt').decode('utf-8').replace('\r', '').split('\n')}
italian_vdb_ad = {a for a in pkgutil.get_data('italian_ats_evaluator', 'nvdb/AD.txt').decode('utf-8').replace('\r', '').split('\n')}
italian_vdb = italian_vdb_fo.union(italian_vdb_au).union(italian_vdb_ad)


spacy_model = None
sentence_transformers_model = None


def get_spacy_model(model_name: str) -> spacy.language.Language:
    global spacy_model
    if spacy_model is None:
        try:
            spacy_model = spacy.load(model_name)
        except OSError:
            spacy.cli.download(model_name)
            spacy_model = spacy.load(model_name)
    return spacy_model


def get_sentence_transformers_model(model_name) -> SentenceTransformer:
    global sentence_transformers_model
    if sentence_transformers_model is None:
        sentence_transformers_model = SentenceTransformer(model_name)
    return sentence_transformers_model


def clean_text(text: str) -> str:
    text = text.strip()
    text = text.replace("\r\n", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")
    return " ".join(text.split())


def eval_syllables(token: str):
    return dic.inserted(token).split('-')


def is_vdb(lemma: str):
    return lemma in italian_vdb


def is_vdb_fo(lemma: str):
    return lemma in italian_vdb_fo


def is_vdb_au(lemma: str):
    return lemma in italian_vdb_au


def is_vdb_ad(lemma: str):
    return lemma in italian_vdb_ad