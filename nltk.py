import nltk
nltk.download('all')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

text = "Natural Language Processing is interesting."
tokens = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

print("Tokens: ", tokens)
print("Removed stop words: ", filtered_tokens)
print("Stemmed tokens: ", stemmed_tokens)

lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Lemmatized tokens: ", lemmatized_tokens)

# POS Tagging
pos_tags = pos_tag(tokens)
print("POS Tags: ", pos_tags)

#pip install nltk
