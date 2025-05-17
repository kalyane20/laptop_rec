# laptop_rec

# 💻 Flipkart Laptop Recommendation Chatbot

This project is an intelligent chatbot built to recommend laptops based on user preferences using the Flipkart laptops dataset. It leverages **Retrieval-Augmented Generation (RAG)**, **LangChain agents**, and **Groq API** to deliver fast and accurate recommendations. The application is built using **Streamlit** for an interactive web interface and **ChromaDB** for vector-based search.

---

## 📁 Project Structure

```plaintext
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
