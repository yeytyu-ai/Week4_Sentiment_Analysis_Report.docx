
import re

def clean_text(text):
    """Clean customer review text for sentiment analysis."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


if __name__ == "__main__":
    sample_review = "This beauty product is AMAZING! I love it."
    print("Original review:", sample_review)
    print("Cleaned review:", clean_text(sample_review))
