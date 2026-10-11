
import csv
from pathlib import Path
from sentiment_analysis import analyze_sentiment


def main():
    input_file = Path("sample_reviews.csv")
    output_file = Path("sentiment_analysis_results.csv")

    with input_file.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or "review" not in reader.fieldnames:
            raise ValueError("CSV must contain a 'review' column.")

        reviews = list(reader)

    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["review", "sentiment"]
        )
        writer.writeheader()

        for row in reviews:
            review = row["review"]
            sentiment = analyze_sentiment(review)
            writer.writerow({
                "review": review,
                "sentiment": sentiment
            })

    print(f"Analysed {len(reviews)} reviews.")
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
