from textblob import TextBlob
from txt_preprocessing import dream_text

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

sentiment = get_sentiment(dream_text)
print(sentiment)
