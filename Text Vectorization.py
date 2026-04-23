from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def basic_nlp_vectorizer():
    # 1. Raw Text Data (Customer Reviews)
    reviews = [
        "The food was excellent and tasty",
        "The food was terrible and slow",
        "Excellent service and fast food",
        "Terrible service, very slow"
    ]

    # 2. Initialize Vectorizer
    # This creates a 'vocabulary' of every unique word
    vectorizer = CountVectorizer()
    
    # 3. Transform text into numbers
    X = vectorizer.fit_transform(reviews)

    # 4. Visualize the Result
    # Each column is a word, each row is a review
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    
    print("--- 📝 Text-to-Number Matrix ---")
    print(df)
    
    print("\nVocabulary mapping:")
    print(vectorizer.vocabulary_)

if __name__ == "__main__":
    basic_nlp_vectorizer()
