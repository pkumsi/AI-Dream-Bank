from txt_preprocessing import preprocess_text, nlp, dream_text

def extract_entities(text):
    doc = nlp(dream_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

entities = extract_entities(preprocess_text)
print(entities)
