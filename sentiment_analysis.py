
from text_preprocessing import clean_text

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "love",
    "happy", "beautiful", "smooth", "best", "effective"
}

NEGATIVE_WORDS = {
    "bad", "poor", "terrible", "hate", "awful",
    "disappointed", "waste", "worst", "irritating", "broken"
}


def analyze_sentiment(review):
    words = clean_text(review).split()

    positive_count = sum(word in POSITIVE_WORDS for word in words)
    negative_count = sum(word in NEGATIVE_WORDS for word in words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    reviews = [
        "This product is amazing and beautiful",
        "This product is terrible",
        "The product arrived today"
    ]

    for review in reviews:
        print(review, "->", analyze_sentiment(review))
