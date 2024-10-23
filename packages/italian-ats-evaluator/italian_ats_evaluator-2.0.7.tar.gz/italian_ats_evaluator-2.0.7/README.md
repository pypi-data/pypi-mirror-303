# italian-ats-evalautor
This is an open source project to evaluate the performance of an italian ATS (Automatic Text Simplifier) on a set of texts.

You can analyze a single text extracting the following features:
- Overall:
  - Number of tokens
  - Number of tokens (including punctuation)
  - Number of characters
  - Number of characters (including punctuation)
  - Number of words
  - Number of syllables
  - Number of unique lemmas
  - Number of sentences
- Readability:
  - Type-Token Ratio (TTR)
  - Gulpease Index
  - Flesch-Vacca Index
  - Lexical Density
- Part of Speech (POS) distribution
- Verbs distribution
  - Active Verbs
  - Passive Verbs
- Italian Basic Vocabulary (NVdB) from [Il Nuovo vocabolario di base della lingua italiana, Tullio De Mauro](https://dizionario.internazionale.it/)
  - All
  - FO (Fundamentals)
  - AU (High Usage)
  - AD (High Availability)


You can also compare two texts and get the following metrics:
- Semantic:
  - Semantic Similarity 
- Character diff:
  - Edit Distance
- Token diff:
  - Amount of tokens added
  - Amount of tokens removed
  - Amount of VdB tokens removed
  - Amount of VdB tokens added


## Installation
```bash
pip install italian-ats-evaluator
```

## Usage

```python
from italian_ats_evaluator import TextAnalyzer

result = TextAnalyzer(
  text="Il gatto mangia il topo",
  spacy_model_name="it_core_news_lg"
)
```

```python
from italian_ats_evaluator import SimplificationAnalyzer

result =  SimplificationAnalyzer(
  reference_text="Il felino mangia il roditore",
  simplified_text="Il gatto mangia il topo",
  spacy_model_name="it_core_news_lg",
  sentence_transformers_model_name="intfloat/multilingual-e5-base"
)
```

## Development
Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
Install the package in editable mode
```bash
pip install -e .
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) “VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility” (Prot. 2020BJKB9M), funded by the Italian Ministero dell’Università e della Ricerca.

## License
[MIT](https://choosealicense.com/licenses/mit/)