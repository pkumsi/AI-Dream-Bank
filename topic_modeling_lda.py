from gensim import corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize
from txt_preprocessing import dream_text, preprocess_text

# Prepare the text for LDA
def prepare_for_lda(text):
    tokens = preprocess_text(text)
    return tokens

tokens = prepare_for_lda(dream_text)

# Create a dictionary and corpus
dictionary = corpora.Dictionary([tokens])
corpus = [dictionary.doc2bow(tokens)]

# LDA model
lda_model = LdaModel(corpus, num_topics=3, id2word=dictionary, passes=15)

# Print topics
topics = lda_model.print_topics(num_words=4)
for topic in topics:
    print(topic)
