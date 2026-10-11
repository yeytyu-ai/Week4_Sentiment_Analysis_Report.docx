
import re

def tokenize_text(text):
    """Split cleaned text into individual words."""
    text = str(text).lower()
    words = re.findall(r"\b[a-z]+\b", text)
    return words


if __name__ == "__main__":
    review = "This beauty product is amazing and easy to use!"
    tokens = tokenize_text(review)
    print("Original review:", review)
    print("Tokens:", tokens)
