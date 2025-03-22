# imports
import streamlit as st
from api import fetch_news, analyze_sentiment, extract_topics, comparative_analysis, generate_audio
# Main Function
def main():
    # Set Up the Streamlit Interface
    st.title("News Summarization & Sentiment Analysis")
    company = st.text_input("Enter Company Name:")
    # Fetch News on Button Click
    if st.button("Fetch News"):
        articles = fetch_news(company)
        
        # Extract sentiment and topics for each article
        topics_per_article = extract_topics(articles)
        for i, article in enumerate(articles):
            article['Sentiment'] = analyze_sentiment(article['Summary'])
            article['Topics'] = topics_per_article[i]
        
        # Perform comparative analysis
        analysis_results = comparative_analysis(articles)
        
        # Display articles with topics and sentiments
        st.subheader("News Articles with Topics and Sentiments")
        st.json(articles)
        
        # Display comparative analysis results
        st.subheader("Comparative Analysis")
        st.json(analysis_results)
        
        # Generate audio for summaries
        summary_texts = [a['Summary'] for a in articles if a['Summary']]
        summary_text_combined = ". ".join(summary_texts)
        
        if summary_text_combined.strip():
            audio_path = generate_audio(summary_text_combined)
            st.audio(audio_path)
        else:
            st.warning("No valid news articles found for the given company.")

if __name__ == "__main__":
    main()