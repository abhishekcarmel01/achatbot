import ollama
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(query):
    results = list(search(query, num_results=1))  
    return results[0] if results else None  

def scrape_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join([para.get_text() for para in paragraphs])
        return content if content else "No relevant content found on the page."
    except Exception as e:
        return f"Error scraping {url}: {e}"

system_message = {"role": "system", "content": "You are a sarcastic AI assistant who gives witty, sassy responses but still provides helpful answers."}
chat_history = [system_message]

def find_in_history(user_input):
    for i in range(len(chat_history) - 1, -1, -1):  
        if chat_history[i]["role"] == "user" and chat_history[i]["content"].lower() == user_input.lower():
            return chat_history[i + 1]["content"] if i + 1 < len(chat_history) else None
    return None  

def summarize_search_results(search_query):
    search_results = google_search(search_query)
    if not search_results:
        print("Chatbot: Oops! No relevant search results found. Maybe try a different query?")
        return

    print(f"Chatbot: Found something! Scraping content from {search_results}...")
    
    content = scrape_content(search_results)

    if content.startswith("Error"):
        print(f"Chatbot: Well, that didn't go as planned. {content}")
        return
    chat_history.append({"role": "user", "content": f"Summarize this webpage content sarcastically: {content[:1000]}"})  
    response = ollama.chat(model="orca-mini", messages=chat_history)

    bot_reply = response["message"]["content"]
    chat_history.append({"role": "assistant", "content": bot_reply})
    print("Chatbot:", bot_reply)

def chat_with_bot():
    print("Hi Abhishek. How can I help you today? Type 'exit' to quit the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Finally, some peace and quiet. Bye!")
            break

        if user_input.startswith("search the web"):
            search_query = user_input.replace("search the web", "").strip()
            summarize_search_results(search_query)
            continue  

        previous_response = find_in_history(user_input)
        if previous_response:
            print("Chatbot:", previous_response)
            continue  

        chat_history.append({"role": "user", "content": user_input})
        response = ollama.chat(model="orca-mini", messages=chat_history)
        bot_reply = response["message"]["content"]
        chat_history.append({"role": "assistant", "content": bot_reply})
        print("Chatbot:", bot_reply)

chat_with_bot()
