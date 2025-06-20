# News Research Analysis Chatbot

A Streamlit chatbot application for research and analysis of news articles using Retrieval-Augmented Generation (RAG) and Google Gemini.

## Features

- Enter one or more news URLs to build a knowledge base.
- Chat with the bot to ask questions about the provided news articles.
- Uses RAG with HuggingFace embeddings and Gemini LLM for concise, accurate answers.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/zer-art/News-Research-Analysis
    
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**
    - Create a `.env` file in the project root:
      ```
      GEMINI_API_KEY=your_google_gemini_api_key
      ```
    - You can get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

4. **Run the app:**
    ```bash
    streamlit run app.py
    ```

## Usage

1. Enter one or more news article URLs (comma separated) in the text area.
2. Click "Load Knowledge Base".
3. Once loaded, ask questions about the news content.

## Project Structure
GitHub Copilot
Here are the recommended contents for your README.md, requirements.txt, and pyproject.toml files:

requirements.txt

pyproject.toml

README.md

. 
├── app.py 
├── src/ 
│ ├── prompt.py 
│ ├── rag.py 
│ └── utils.py 
├── requirements.txt 
├── pyproject.toml 
└── README.md


## Notes

- For best results, use direct links to news articles, not homepages.
- If you encounter errors with document loading, try different URLs.

