# app.py

from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the Flask app
app = Flask(__name__)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define the sentiment analysis function
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    print(request.form)  # Print form data for debugging
    if 'text' not in request.form:
        return "No text found in form data", 400  # Return 400 error if 'text' key is missing
    
    text = request.form['text']
    sentiment_scores = analyze_sentiment(text)

    sentiment_type = 'Neutral'
    if sentiment_scores['compound'] > 0:
        sentiment_type = 'Positive'
    elif sentiment_scores['compound'] < 0:
        sentiment_type = 'Negative'

    return render_template('index.html', text=text, sentiment=sentiment_type)

if __name__ == '__main__':
    app.run(port=5001)
