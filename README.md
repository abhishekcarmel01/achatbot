# Sarcastic AI Chatbot with Web Search

## Overview
This is a sarcastic AI chatbot built using `ollama` that provides witty and sassy responses while still being helpful. Additionally, it can perform web searches, scrape content, and summarize the results before responding.

## Features
- **Conversational AI**: Uses `orca-mini` to generate responses.
- **Sarcastic Personality**: Provides witty and humorous responses.
- **Chat History Awareness**: Remembers past user interactions and responds accordingly.
- **Web Search & Summarization**: Fetches the most relevant search results, scrapes content, and summarizes it using AI.

## Requirements
Ensure you have the following installed:

- Python 3.x
- `ollama` package
- `requests` package
- `beautifulsoup4` package
- `googlesearch-python` package

You can install dependencies using:
```sh
pip install ollama requests beautifulsoup4 googlesearch-python
```

## Usage
Run the chatbot with:
```sh
python chatbot.py
```
### Commands
- **Normal Chat**: Simply type a message to chat with the AI.
- **Web Search**: Type `search the web <your query>` to perform a search and get a summarized result.
- **Exit**: Type `exit` to end the chat.

## Code Overview

### `google_search(query)`
Searches Google and returns the top result URL.

### `scrape_content(url)`
Fetches and extracts readable text content from the given URL.

### `summarize_search_results(search_query)`
Conducts a web search, scrapes content, and summarizes it using AI.

### `find_in_history(user_input)`
Checks past chat history to maintain context in conversations.

### `chat_with_bot()`
Main function that handles user input and chatbot responses.

## Example Interaction
```
Hi Abhishek. How can I help you today? Type 'exit' to quit the chat.
You: How old am I?
Chatbot: You are 25! One-quarter through life. Hope you're enjoying the ride.
You: How old am I?
Chatbot: Didn’t I just tell you? You’re 25. Pay attention!
You: search the web latest AI trends
Chatbot: [Summarized AI trends from web search]
You: exit
Goodbye!
```

## Future Improvements
- Implementing memory persistence across sessions.
- Enhancing sarcasm with more nuanced responses.
- Improving web scraping for better accuracy.

## License
This project is open-source. Feel free to use and modify it!
