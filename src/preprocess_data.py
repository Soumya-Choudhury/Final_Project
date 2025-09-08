import re, string
import pandas as pd

def clean_text(text):
    """Remove URLs, mentions, hashtags, punctuation, and lowercase."""
    text = re.sub(r"http\S+|www\.\S+", "", str(text))
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()

def preprocess_data(df):
    """Fill missing values and clean message text."""
    df.dropna(subset=["message", "sentiment_type"], inplace=True)
    df["message"] = df["message"].fillna("missing_message")
    df["message_clean"] = df["message"].map(clean_text)
    return df
