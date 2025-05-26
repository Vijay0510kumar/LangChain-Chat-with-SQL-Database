#  LangChain SQL Chatbot — Natural Language to SQL

A Streamlit-based AI chatbot that allows users to interact with structured SQL databases using natural language queries. It leverages **LangChain** with **Groq's Llama3-8b-8192** model to convert natural language into SQL statements and retrieve data seamlessly from **SQLite** or **MySQL** databases.

---

##  Overview

This project showcases the transformative potential of Large Language Models (LLMs) in democratizing data access by bridging the gap between human language and structured database querying. Traditionally, interacting with databases requires knowledge of SQL, table relationships, and schema structure—barriers that can hinder data exploration for non-technical users.

With this AI-powered interface, users can simply type natural language questions such as:

“What were the total sales for last month?”

“List all active employees in the HR department.”

“Show top 5 customers by order volume this quarter.”

Behind the scenes, the app intelligently converts these queries into accurate SQL statements, executes them against the connected database, and returns clean, readable results—all without requiring the user to know anything about SQL syntax or schema logic.

 Who Is This For?
This tool is ideal for:

 Data Analysts who want to quickly extract insights without writing queries manually.

 Business Users or Executives who need quick answers from enterprise databases.

 Developers looking to prototype LLM + SQL integrations for intelligent dashboards.

 Students and Educators seeking to explore how natural language processing meets data querying.

 Operations/Support Teams who frequently request data from engineering or analytics teams..

---

##  Features

| Feature                         | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
|   Natural Language Chat        | Interact with any SQL database by asking plain-English questions           |
|   SQLite & MySQL Support       | Choose between a local SQLite file or a remote MySQL database              |
|   Groq Llama3-8b-8192 Model    | Uses LangChain and Groq API for high-speed, accurate SQL generation        |
|   Streamlit Chat UI            | Interactive, web-based chat interface with real-time responses             |
|   Secure API Key Entry         | Users enter their Groq API key directly in the UI to start the session     |
|   Dynamic Schema Inference     | Bot reads your DB schema to create accurate, context-aware SQL queries     |
|   Result Table Display         | SQL output is shown as a table directly within the Streamlit app           |

---

##  How It Works

1. **User Query**: The user enters a natural language question.
2. **Schema Awareness**: The app uses `SQLDatabase.from_uri()` to let the LLM access schema context.
3. **LLM Conversion**: LangChain sends the query and schema to Groq’s Llama3-8b-8192 model.
4. **SQL Generation**: The model returns a valid SQL query.
5. **Execution**: SQLAlchemy executes the query and returns results.
6. **Display**: Streamlit displays the results in a readable table format.

---

##  Tech Stack

- **Python 3.10+**
- **LangChain**
- **Streamlit**
- **SQLAlchemy**
- **SQLite / MySQL**
- **Groq LLM (Llama3-8b-8192)**

---
![Uploading SQL_chatbot.jpg…]()

