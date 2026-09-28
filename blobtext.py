from textblob import TextBlob

reviews = [
    "I love this product. It is amazing!",
    "The product is good and useful.",
    "The product is okay.",
    "I hate this product. It is terrible!",
    "The product is not good."
]

for review in reviews:
    blob = TextBlob(review)

    print("Review:", review)
    print("Sentiment:", blob.sentiment)
    print("Polarity:", blob.sentiment.polarity)
    print("Subjectivity:", blob.sentiment.subjectivity)

#pip install textblob      
