
from collections import Counter
from sentiment_analysis import analyze_sentiment


def calculate_sentiment_percentage(reviews):
    sentiments = [analyze_sentiment(review) for review in reviews]
    total = len(sentiments)

    if total == 0:
        print("No reviews available.")
        return

    counts = Counter(sentiments)

    for sentiment in ["Positive", "Negative", "Neutral"]:
        count = counts.get(sentiment, 0)
        percentage = (count / total) * 100
        print(f"{sentiment}: {count} reviews ({percentage:.2f}%)")


if __name__ == "__main__":
    reviews = [
        "Amazing beauty product",
        "Very poor quality",
        "The product arrived today",
        "I love this product",
        "This product is terrible"
    ]

    calculate_sentiment_percentage(reviews)
