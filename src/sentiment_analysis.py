import torch
from transformers import BertTokenizer, BertForSequenceClassification
from datasets import load_from_disk

# Load model and tokenizer
model_path = './models/sentiment_model'
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

# Load processed data
processed_data_dir = 'data/processed/'
dataset = load_from_disk(processed_data_dir)

# Predict sentiment
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    sentiment = 'Positive' if prediction == 1 else 'Negative' if prediction == 0 else 'Neutral'
    return sentiment

# Apply to dataset
dataset = dataset.map(lambda x: {'sentiment': predict_sentiment(x['text'])})
dataset.save_to_disk(processed_data_dir)
