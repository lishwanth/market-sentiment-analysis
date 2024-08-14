
# Market Sentiment Analysis and Trend Prediction

## Project Overview

This project aims to perform market sentiment analysis by leveraging a pre-trained BERT model to analyze customer reviews and social media data. The project includes data collection, preprocessing, sentiment analysis, trend analysis, and deployment. The final product is a deployable model with a user-friendly front-end interface.

## Features

- **Data Collection and Preprocessing**: Collects and preprocesses datasets from sources like Amazon Reviews.
- **Sentiment Analysis**: Uses a pre-trained BERT model to classify sentiments as Positive, Negative, or Neutral.
- **Trend Analysis**: Visualizes sentiment trends over time to identify patterns.
- **Deployment**: The model is deployed as an API with a Streamlit front-end for easy interaction.

## Project Structure

```
market-sentiment-analysis/
│
├── data/
│   ├── raw/                   # Raw datasets
│   ├── processed/             # Processed datasets ready for analysis
│   └── download_datasets.py   # Script to download and preprocess datasets
│
├── notebooks/
│   ├── exploratory_analysis.ipynb   # EDA and data exploration
│   ├── sentiment_analysis.ipynb     # Sentiment analysis using the pre-trained model
│   ├── trend_analysis.ipynb         # Trend analysis and visualization
│
├── models/
│   └── sentiment_model/             # Directory for storing the pre-trained model
│
├── src/
│   ├── data_preprocessing.py        # Script for data preprocessing
│   ├── sentiment_analysis.py        # Script for applying the pre-trained model to new data
│   ├── trend_analysis.py            # Script for trend analysis
│   ├── api.py                       # Flask API for serving the model
│   └── front_end.py                 # Streamlit front-end interface
│
├── Dockerfile                       # Dockerfile for containerization
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── LICENSE                          # License file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lishwanth/market-sentiment-analysis.git
    cd market-sentiment-analysis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and preprocess datasets:
    ```bash
    python data/download_datasets.py
    python src/data_preprocessing.py
    ```

4. Run the notebooks in the following order:
    1. `notebooks/exploratory_analysis.ipynb`
    2. `notebooks/sentiment_analysis.ipynb`
    3. `notebooks/trend_analysis.ipynb`

### Running the Application

1. **Run the Flask API:**
    ```bash
    python src/api.py
    ```

2. **Run the Streamlit front-end:**
    ```bash
    streamlit run src/front_end.py
    ```

### Docker Deployment

To deploy the application using Docker:

1. Build the Docker image:
    ```bash
    docker build -t market-sentiment-analysis .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 market-sentiment-analysis
    ```

## Usage

- Access the API at `http://localhost:5000/predict` to get sentiment predictions.
- Use the Streamlit front-end to interact with the model by entering text and viewing sentiment results.

## Results

- The project provides insights into customer sentiments over time, helping businesses identify trends and areas for improvement.
- Visualizations of sentiment trends are available in the `notebooks/trend_analysis.ipynb`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. Your contributions are welcome!

## Contact

For any inquiries or issues, please contact [Lishwanth] at [lishwanthkumar@gmail.com].
