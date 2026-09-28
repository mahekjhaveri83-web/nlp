import stanza

stanza.download("en")

nlp = stanza.Pipeline("en")

text = "The boy eats an apple. The girl reads a book. The dog runs quickly."
doc = nlp(text)

# Task 9: POS Tagging with Stanza
for sen in doc.sentences:
    for word in sen.words:
        print(word.text, word.upos)

# Task 10: Dependency Parsing
for sen in doc.sentences:
    for word in sen.words:
        print(word.text, word.head, word.deprel)

#pip install stanza        
