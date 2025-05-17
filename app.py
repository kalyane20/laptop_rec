import os
import streamlit as st
import pandas as pd
import datetime
from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from langchain_community.document_loaders import DataFrameLoader
from langchain.chains import RetrievalQA
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
os.environ.setdefault("GROQ_API_KEY", os.getenv("GROQ_API_KEY", "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"))
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("flipkart_laptops_enriched.csv")
        if df.empty:
            st.warning("The dataset is empty.")
        return df
    except FileNotFoundError:
        st.error("Dataset file flipkart_laptops_enriched.csv not found!")
        return pd.DataFrame()

@st.cache_resource
def setup_retriever(df):
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    persist_dir = "chroma_db"

    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        db = Chroma(persist_directory=persist_dir, embedding_function=embedding)
    else:
        loader = DataFrameLoader(df[['text']], page_content_column="text")
        docs = loader.load()
        db = Chroma.from_documents(docs, embedding, persist_directory=persist_dir)
    return db.as_retriever()

def setup_agent(retriever):
    llm = ChatOpenAI(model="llama3-8b-8192", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    tools = [
        Tool(
            name="LaptopSearch",
            func=qa_chain.run,
            description="Search and recommend laptops from Flipkart dataset"
        )
    ]

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
    )
    return agent, memory

# Streamlit UI setup
st.set_page_config(page_title="Flipkart Laptop Chatbot", page_icon="💻")
st.title("💻 Flipkart Laptop Recommendation Chatbot (Groq + LangChain)")
st.markdown("""
Type questions like:
- Suggest laptops under ₹50000
- Best lightweight laptop with SSD
- Gaming laptops with i7 processor
""")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "agent" not in st.session_state or "memory" not in st.session_state:
    df = load_data()
    if df.empty:
        st.stop()  # Stop if dataset loading failed or empty
    retriever = setup_retriever(df)
    st.session_state.agent, st.session_state.memory = setup_agent(retriever)

agent = st.session_state.agent

# Clear chat history button
if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()

# Show info if chat is empty
if not st.session_state.chat_history:
    st.info("Ask me anything about Flipkart laptops!")

user_input = st.chat_input("Ask your laptop query here...")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = agent.run(user_input)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            response = "Sorry, something went wrong."
    st.session_state.chat_history.append((user_input, response))

# Display chat history
for q, a in st.session_state.chat_history:
    st.chat_message("user").write(q)
    st.chat_message("assistant").write(a)

# Save chat history to file
if st.button("💾 Save Chat"):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"chat_history_{ts}.txt", "w", encoding="utf-8") as f:
        for q, a in st.session_state.chat_history:
            f.write(f"User: {q}\nBot: {a}\n\n")
    st.success("Chat history saved.")
