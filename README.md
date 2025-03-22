# Company News Summarization and Sentiment Analysis

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
 <img width="589" alt="image" src="https://github.com/user-attachments/assets/90e566fe-5aa3-4b33-a276-5e0eef9b94af" />   
 
	2.	Create and activate a virtual environment:  
 <img width="226" alt="image" src="https://github.com/user-attachments/assets/45876e0d-2270-4c9b-9ab5-7da250f03614" />   
 
 		On Windows:
   <img width="222" alt="image" src="https://github.com/user-attachments/assets/cdb75060-dbf1-4d9f-9a5e-13ed3bdeeefa" />  

 	3.	Install the required dependencies:  
  <img width="300" alt="image" src="https://github.com/user-attachments/assets/faebe0ce-0443-4e75-9e6e-164b2bd70ea7" />  

  	4.	Set up your News API key:  
		•	Sign up for a free API key at https://newsapi.org/  
		•	Replace `NEWS_API_KEY` in `api.py` with your actual API key. 
  
  	5.	Run the application:  
   <img width="207" alt="image" src="https://github.com/user-attachments/assets/97239afe-935e-4dba-9fb8-3d108974bad7" />  
   
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

Model Details

Summarization Model  

The summarization functionality of the application relies on TF-IDF (Term Frequency-Inverse Document Frequency) combined with KMeans clustering.  

	•	TF-IDF is used to vectorize the text data (news article summaries) by transforming text into numerical vectors based on word frequency and its importance within the entire document set.  
	•	KMeans clustering is used to cluster articles into different topics based on their vectorized summary data. It helps in grouping articles that are related to similar topics.  

Sentiment Analysis Model  

The sentiment analysis is performed using the TextBlob library, which is a simple library for processing textual data. The sentiment polarity score is used to determine the overall sentiment of the article's summary.  

Sentiment Classification  

Positive: If the sentiment score is greater than 0.  
Negative: If the sentiment score is less than 0.  
Neutral: If the sentiment score equals 0.  

Text-to-Speech (TTS) Model  

The Google Text-to-Speech (gTTS) library is used to convert the news summaries into audio. This library provides an easy way to convert text to speech and supports multiple languages, including Hindi.

gTTS generates the audio file from the text and saves it as an MP3 file that can be played in the browser via Streamlit.

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
 
NewsAPI Integration  

The NewsAPI is used to fetch the latest news articles related to a specific company. Here's how you can use it and test the endpoint via Postman or any other tool:  

URL: https://newsapi.org/v2/everything  

Parameters:  

	•	q=<company_name>: Replace <company_name> with the company name you want to search for.  
	•	apiKey=<your_api_key>: Replace <your_api_key> with your actual NewsAPI key.  
	•	language=en: Set the language to English to fetch English articles.  

Example API Request:  

<img width="721" alt="image" src="https://github.com/user-attachments/assets/071bec8b-7b3a-41d7-9dbc-44271b0c6c81" />  

Postman Configuration:  

	•	Set the request method to GET.  
	•	Enter the URL as above.  
	•	Click Send to retrieve the latest articles related to Microsoft  
	•	You'll receive a JSON response with articles that you can further process.  

Limitations and Assumptions  

	•	The application assumes a stable internet connection for fetching news and API access.
	•	The sentiment analysis is basic and might not be as accurate for complex texts.  
	•	The application is designed for English news articles, with translation to Hindi for TTS. The translation may not be perfectly accurate.  
 
Deployment  
The application is deployed on Hugging Face Spaces. You can access it at https://huggingface.co/spaces/hugginggoku/company-sentiment-analysis
