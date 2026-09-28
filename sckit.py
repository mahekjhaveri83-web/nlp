from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love machine learning",
    "Machine learning is interesting",
    "I love artificial intelligence"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print("TF-IDF Matrix:")
print(X.toarray())

#pip install scikit-learn
