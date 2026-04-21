from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def build_sentiment_bot():
    # 1. Training Data
    X_train = [
        "I love this product, it works great",
        "Absolutely fantastic experience",
        "Worst purchase ever, I hate it",
        "Do not buy this, it is broken and bad",
        "Simply amazing quality",
        "Total waste of money"
    ]
    y_train = ["Positive", "Positive", "Negative", "Negative", "Positive", "Negative"]

    # 2. Create a Pipeline
    # Tfidf (Term Frequency-Inverse Document Frequency) is a smarter way 
    # to weight words, making rare words like 'fantastic' more important.
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # 3. Train
    model.fit(X_train, y_train)

    # 4. Test on new, unseen text
    new_reviews = ["This is amazing!", "it is broken", "great quality"]
    predictions = model.predict(new_reviews)

    print("--- 🤖 Sentiment Analysis Results ---")
    for review, sentiment in zip(new_reviews, predictions):
        print(f"Review: '{review}' -> {sentiment}")

if __name__ == "__main__":
    build_sentiment_bot()
