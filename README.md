# News-Summarization
Overview
This application extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. Users can input a company name and receive a structured sentiment report along with an audio output.  

Features  
	•	News extraction from multiple sources  
	•	Sentiment analysis of article content  
	•	Comparative analysis across articles  
	•	Text-to-speech conversion to Hindi  
	•	Web-based user interface  
	•	API-based communication between frontend and backend  
Dependencies  
The application requires the following main dependencies:  
	•	Python 3.7+  
	•	requests  
	•	beautifulsoup4  
	•	textblob  
	•	scikit-learn  
	•	gTTS  
	•	deep_translator  
	•	streamlit  
  	•	newspaper3k  
	•	nltk  
For a complete list of dependencies, refer to the `requirements.txt` file.  
Setup Instructions  
	1.	Clone the repository:  
 <img width="507" alt="image" src="https://github.com/user-attachments/assets/f06695e1-c61e-4e81-b7ab-f8a760d10e22" />
	2.	Create and activate a virtual environment:
 	3.	Install the required dependencies:
  	4.	Set up your News API key:
		•	Sign up for a free API key at https://newsapi.org/
		•	Create a `.env` file in the project root and add your API key:
  	5.	Run the application:  
   <img width="292" alt="image" src="https://github.com/user-attachments/assets/0e2bcc19-0bc2-44d1-b2da-6f30f7edefbc" />  
   Implementation Details
News Extraction
The application uses the News API to fetch recent articles related to the input company name. It extracts the title, summary, and other relevant metadata from at least 10 unique news articles.
Sentiment Analysis
Sentiment analysis is performed on the article content using TextBlob. Each article is categorized as positive, negative, or neutral based on its sentiment score.
Comparative Analysis
The application conducts a comparative sentiment analysis across the articles to derive insights on how the company’s news coverage varies. This includes sentiment distribution and coverage differences between articles.
Text-to-Speech
The summarized content is converted into Hindi speech using gTTS (Google Text-to-Speech) and deep_translator for translation.
User Interface
The web-based interface is built using Streamlit. Users can input a company name to fetch news articles and generate the sentiment report.
API Development
The communication between the frontend and backend happens via APIs defined in `api.py`. These APIs handle news fetching, sentiment analysis, and text-to-speech conversion.  

File Structure
	•	`app.py`: Main application script
	•	`api.py`: API definitions for backend communication
	•	`utils.py`: Utility functions for data processing
	•	`requirements.txt`: List of project dependencies
	•	`README.md`: Project documentation
Usage
	1.	Run the application using `streamlit run app.py`
	2.	Enter a company name in the input field
	3.	Click the “Fetch News” button
	4.	View the structured report with article summaries, sentiments, and comparative analysis
	5.	Listen to the Hindi TTS output summarizing the sentiment report
Limitations and Assumptions
	•	The application assumes a stable internet connection for fetching news and API access.
	•	Sentiment analysis accuracy may vary depending on the complexity of the news content.
	•	The application is designed for English news articles, with translation to Hindi for TTS.
Future Enhancements
	•	Support for multiple languages in news extraction and analysis
	•	Integration with additional news sources
	•	Improved summarization techniques using advanced NLP models
	•	Enhanced visualization of sentiment trends over time  
Deployment  
The application is deployed on Hugging Face Spaces. You can access it at https://huggingface.co/spaces/hugginggoku/company-sentiment-analysis
