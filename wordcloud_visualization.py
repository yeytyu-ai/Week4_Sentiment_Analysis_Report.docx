
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from text_preprocessing import clean_text


def generate_wordcloud(reviews):
    cleaned_reviews = [clean_text(review) for review in reviews]
    text = " ".join(cleaned_reviews)

    if not text.strip():
        print("No text available to generate a word cloud.")
        return

    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Frequently Used Words in Customer Reviews")
    plt.tight_layout()
    plt.savefig("wordcloud.png")
    plt.show()


if __name__ == "__main__":
    reviews = [
        "Amazing beauty product with great quality",
        "This product makes my skin smooth",
        "Poor quality and disappointing results",
        "I love this product and its quality",
        "Good product for beauty and wellness"
    ]

    generate_wordcloud(reviews)
