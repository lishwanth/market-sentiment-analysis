import os
from datasets import load_dataset
import spacy

# Load English tokenizer
nlp = spacy.load("en_core_web_sm")

# Download dataset
def download_dataset():
    dataset = load_dataset('amazon_polarity')
    raw_data_dir = 'data/raw/'
    if not os.path.exists(raw_data_dir):
        os.makedirs(raw_data_dir)
    dataset.save_to_disk(raw_data_dir)
    print(f"Dataset saved to {raw_data_dir}")

# Preprocess text
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Apply preprocessing
def preprocess_dataset():
    dataset = load_dataset('amazon_polarity')
    processed_data_dir = 'data/processed/'
    dataset = dataset.map(lambda x: {'text': preprocess_text(x['content'])})
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    dataset.save_to_disk(processed_data_dir)
    print(f"Processed dataset saved to {processed_data_dir}")

if __name__ == "__main__":
    download_dataset()
    preprocess_dataset()
