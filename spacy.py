import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple is opening a new office in Mumbai."
doc = nlp(text)

for token in doc:
    print(token.text, token.pos_)

for ent in doc.ents:
    print(ent.text, ent.label_)

# Task 8: Entity Frequency
from collections import Counter

entity_freq = Counter([ent.text for ent in doc.ents])

for entity, frequency in entity_freq.items():
    print(entity, ":", frequency)

#pip install spacy    
