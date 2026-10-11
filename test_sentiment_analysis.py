
import unittest
from sentiment_analysis import analyze_sentiment


class TestSentimentAnalysis(unittest.TestCase):

    def test_positive_review(self):
        self.assertEqual(
            analyze_sentiment("This product is amazing"),
            "Positive"
        )

    def test_negative_review(self):
        self.assertEqual(
            analyze_sentiment("This product is terrible"),
            "Negative"
        )

    def test_neutral_review(self):
        self.assertEqual(
            analyze_sentiment("The product arrived today"),
            "Neutral"
        )

    def test_empty_review(self):
        self.assertEqual(analyze_sentiment(""), "Neutral")


if __name__ == "__main__":
    unittest.main()
