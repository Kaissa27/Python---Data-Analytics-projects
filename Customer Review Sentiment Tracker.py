def analyze_feedback():
    # Raw Data: [Review_Text]
    reviews = [
        "The product is amazing and very fast!",
        "Terrible experience, the item arrived broken.",
        "It is okay, does the job but nothing special.",
        "I love this! Best purchase of the year.",
        "Slow shipping and bad customer service.",
        "Decent quality for the price.",
        "Absolutely hated it. Waste of money."
    ]

    # 1. Define Sentiment Keywords
    positive_words = ["amazing", "fast", "love", "best", "decent", "good"]
    negative_words = ["terrible", "broken", "slow", "bad", "hated", "waste"]

    # 2. Results Container
    report = {"Positive": 0, "Negative": 0, "Neutral": 0}

    print("--- Customer Sentiment Analysis ---")
    
    for text in reviews:
        # Clean text: lowercase and remove punctuation for better matching
        clean_text = text.lower().replace(".", "").replace("!", "")
        words = clean_text.split()

        # 3. Logic: Check which list has more matches in the review
        pos_hits = sum(1 for word in words if word in positive_words)
        neg_hits = sum(1 for word in words if word in negative_words)

        if pos_hits > neg_hits:
            sentiment = "Positive"
        elif neg_hits > pos_hits:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        report[sentiment] += 1
        print(f"Review: \"{text}\" -> [{sentiment}]")

    # 4. Final Aggregation
    print("-" * 40)
    print("Final Sentiment Distribution:")
    for category, count in report.items():
        # Simple text-based bar chart
        bar = "█" * count
        print(f"{category:<8}: {bar} ({count})")

analyze_feedback()