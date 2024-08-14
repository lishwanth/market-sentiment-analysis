import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_from_disk

# Load processed dataset
processed_data_dir = 'data/processed/'
dataset = load_from_disk(processed_data_dir)

# Convert date to datetime
dataset['train']['date'] = pd.to_datetime(dataset['train']['date'])

# Sentiment over time
sentiment_over_time = dataset['train'].groupby(dataset['train']['date'].dt.to_period('M')).mean()

# Plot sentiment trends
sentiment_over_time.plot()
plt.title('Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment')
plt.show()
