# laptop_rec

# 💻 Flipkart Laptop Recommendation Chatbot

This project is an intelligent chatbot built to recommend laptops based on user preferences using the Flipkart laptops dataset. It leverages **Retrieval-Augmented Generation (RAG)**, **LangChain agents**, and **Groq API** to deliver fast and accurate recommendations. The application is built using **Streamlit** for an interactive web interface and **ChromaDB** for vector-based search.


# 📁 Project Structure

``plaintext
├── enrich.py              # Script to enrich and preprocess the dataset             # Main Streamlit app for chatbot interface

├── app.py                 # Main Streamlit app for chatbot interface
├── flipkart_laptops_dataset.csv  # Original dataset from Flipkart
├── flipkart_laptops_enriched.csv # Cleaned and enriched dataset used for RAG
├── requirements.txt              # List of Python dependencies



##Tech Stack
Language: Python

Frontend: Streamlit

LLM: Groq API (preferred over OpenAI for faster responses)

RAG & Agents: LangChain

Vector DB: ChromaDB

Development Tools: Jupyter Notebook, VSCode


⚙️ Features

🔍 Smart laptop recommendations from Flipkart dataset


💬 Conversational chatbot using LangChain and Groq

🧠 Retrieval-Augmented Generation for accurate context-aware responses

🧰 LangChain agents to handle tool use and decision-making

💾 Chat history support (optional for extended UX)

⚡ Fast, lightweight local deployment with Groq


 # How to Run the Project
 
###Clone the Repository:

---git clone https://github.com/your-username/flipkart-laptop-chatbot.git
cd flipkart-laptop-chatbot  ---


###Install Dependencies:

---pip install -r requirements.txt---


###Set Your Groq API Key:

---export GROQ_API_KEY=your_key_here  # for Linux/macOS
set GROQ_API_KEY=your_key_here     # for Windows (CMD)---


###Run the App:

---streamlit run app.py---




