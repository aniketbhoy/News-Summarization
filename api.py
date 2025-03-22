# imports
import requests
from textblob import TextBlob
from gtts import gTTS
from deep_translator import GoogleTranslator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# API Key for News API
NEWS_API_KEY = "4ba00321cab44fdaab53314eaab6d8c5"

# fetch_news Function
def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url).json()
    
    articles = []
    for item in response.get("articles", [])[:10]:  # Fetch up to 10 articles
        articles.append({
            "Title": item["title"],
            "Summary": item["description"] or "No summary available."
        })
    
    return articles

# analyze_sentiment Function
def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
# extract_topics Function
def extract_topics(articles):
    vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([a['Summary'] for a in articles if a['Summary']])
    
    num_clusters = min(3, len(articles))
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    
    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    
    topics_per_article = []
    for i, article in enumerate(articles):
        if article['Summary']:
            cluster_idx = kmeans.predict(tfidf_matrix[i])
            topic_terms = [terms[ind] for ind in order_centroids[cluster_idx[0], :5]]
            topics_per_article.append(topic_terms)
        else:
            topics_per_article.append(["No significant topics"])
    
    return topics_per_article
# comparative_analysis Function
def comparative_analysis(articles):
    comparisons = []
    sentiments = [analyze_sentiment(a['Summary']) for a in articles]
    
    for i in range(len(articles) - 1):
        comparison = {
            "Comparison": f"Article {i+1} discusses '{articles[i]['Title']}' while Article {i+2} focuses on '{articles[i+1]['Title']}'.",
            "Impact": f"Sentiment of Article {i+1} is {sentiments[i]}, while Article {i+2} is {sentiments[i+1]}."
        }
        comparisons.append(comparison)
    
    sentiment_distribution = {
        "Positive": sentiments.count("Positive"),
        "Negative": sentiments.count("Negative"),
        "Neutral": sentiments.count("Neutral")
    }
    
    return {
        "Coverage Differences": comparisons,
        "Sentiment Distribution": sentiment_distribution,
        "Overall Sentiment": max(sentiment_distribution, key=sentiment_distribution.get)
    }
# generate_audio Function
def generate_audio(text):
    translated_text = GoogleTranslator(source='en', target='hi').translate(text)
    tts = gTTS(translated_text, lang='hi')
    audio_path = "output.mp3"
    tts.save(audio_path)
    return audio_path