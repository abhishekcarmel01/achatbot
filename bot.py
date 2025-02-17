import ollama
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(query):
    results = search(query, num_results=1) 
    return "\n".join(results)

def scrape_content(url):
   # print(f"Scraping {url}...")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join([para.get_text() for para in paragraphs])
        return content
    except Exception as e:
        return f"Error scraping {url}: {e}"
    

system_message = {"role": "system", "content": "You are a sarcastic AI assistant who gives witty, sassy responses but still provides helpful answers."}
chat_history=[system_message]

def summarize_search_results(search_query):
    search_results = google_search(search_query)  
    #print(search_results)  
    summarized_content = ""
    content = scrape_content(search_results)
    summarized_content += content + "\n\n"
    #print (summarized_content)
    response = ollama.chat(model="orca-mini", messages=[{"role": "system", "content": "Summarize the following content:"}, {"role": "user", "content": summarized_content}])
    return response["message"]["content"]

def chat_with_bot():
    print("Hi Abhishek. How can I help you today? Type 'exit' to quit the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.startswith("search the web"):
            search_query = user_input.replace("search the web", "").strip()
            response = summarize_search_results(search_query)
            print("Chatbot:", response)
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": response})
            continue
        chat_history.append({"role": "user", "content": user_input})
        response = ollama.chat(model="orca-mini", messages=[{"role": "user", "content": user_input}])
        chat_history.append({"role":"assistant", "content": response["message"]["content"]})
        print("Chatbot:", response["message"]["content"])

chat_with_bot()
