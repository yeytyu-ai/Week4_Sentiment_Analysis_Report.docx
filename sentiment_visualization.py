
import matplotlib.pyplot as plt
from collections import Counter
from sentiment_analysis import analyze_sentiment


def plot_sentiment_distribution(reviews):
    sentiments = [analyze_sentiment(review) for review in reviews]
    counts = Counter(sentiments)

    labels = ["Positive", "Negative", "Neutral"]
    values = [counts.get(label, 0) for label in labels]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Customer Review Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig("sentiment_distribution.png")
    plt.show()


if __name__ == "__main__":
    reviews = [
        "Amazing beauty product",
        "Very poor quality",
        "The product arrived today",
        "I love this product",
        "This product is terrible"
    ]

    plot_sentiment_distribution(reviews)
