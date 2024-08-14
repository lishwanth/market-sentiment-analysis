from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = Flask(__name__)

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained('./models/sentiment_model')
tokenizer = BertTokenizer.from_pretrained('./models/sentiment_model')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = tokenizer(data['text'], return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    sentiment = 'Positive' if prediction == 1 else 'Negative' if prediction == 0 else 'Neutral'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
