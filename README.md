# 🦜 LangChain SQL Chatbot — Natural Language to SQL

A Streamlit-based AI chatbot that allows users to interact with structured SQL databases using natural language queries. It leverages **LangChain** with **Groq's Llama3-8b-8192** model to convert natural language into SQL statements and retrieve data seamlessly from **SQLite** or **MySQL** databases.

---

## 📌 Overview

This project demonstrates the power of **LLMs (Large Language Models)** in democratizing access to database systems. Non-technical users can ask questions like “What were the total sales last month?” or “List all active employees in the HR department” without writing a single line of SQL.

✅ Ideal for data analysts, business users, or developers who want a natural language interface for databases.

---

## ✨ Features

| Feature                         | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| 🗨️ Natural Language Chat        | Interact with any SQL database by asking plain-English questions           |
| 🛠️ SQLite & MySQL Support       | Choose between a local SQLite file or a remote MySQL database              |
| 🧠 Groq Llama3-8b-8192 Model    | Uses LangChain and Groq API for high-speed, accurate SQL generation        |
| 💬 Streamlit Chat UI            | Interactive, web-based chat interface with real-time responses             |
| 🔐 Secure API Key Entry         | Users enter their Groq API key directly in the UI to start the session     |
| 📚 Dynamic Schema Inference     | Bot reads your DB schema to create accurate, context-aware SQL queries     |
| 📈 Result Table Display         | SQL output is shown as a table directly within the Streamlit app           |

---

## 🧠 How It Works

1. **User Query**: The user enters a natural language question.
2. **Schema Awareness**: The app uses `SQLDatabase.from_uri()` to let the LLM access schema context.
3. **LLM Conversion**: LangChain sends the query and schema to Groq’s Llama3-8b-8192 model.
4. **SQL Generation**: The model returns a valid SQL query.
5. **Execution**: SQLAlchemy executes the query and returns results.
6. **Display**: Streamlit displays the results in a readable table format.

---

## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain**
- **Streamlit**
- **SQLAlchemy**
- **SQLite / MySQL**
- **Groq LLM (Llama3-8b-8192)**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-sql-chatbot.git
cd langchain-sql-chatbot
