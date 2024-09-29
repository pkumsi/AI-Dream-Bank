import spacy
from nltk.corpus import stopwords
import string

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Example dream input
dream_text = """
First, I was singing in the My school Choir. Then my friend Anna and I went up to the bathroom. 
For some strange reason, when you pulled the paper towels out, water squirted you in the face. 
I got squirted. Then we were transported into a desert. I got cut on three thorns. 
We were trying to get back to My school. Then we came to the top of a building. We were on top. 
We looked over the edge. There was Bobbie's room. Bobbie and her husband, who said he was 1 zillion years old, came out. 
Bobbie said, "This hasn't happened in years!" Then they lifted us down.
"""

def preprocess_text(text):
    # Use SpaCy to process the text
    doc = nlp(text)

    # Lemmatization, removing stopwords and punctuation
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    # Lowercase all tokens
    tokens = [token.lower() for token in tokens]

    return tokens

preprocessed_text = preprocess_text(dream_text)
print(preprocessed_text)
