import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

# -------------------- Streamlit Page Setup -------------------- #
st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL Database")

# -------------------- Database Selection -------------------- #
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_opt = ["Use SQLite3 Database - student.db", "Connect to your MySQL Database"]
selected_opt = st.sidebar.radio("Choose Database Option:", radio_opt)

if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("MySQL Host", placeholder="e.g. localhost")
    mysql_user = st.sidebar.text_input("MySQL User", placeholder="e.g. root")
    mysql_password = st.sidebar.text_input("MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database Name")
else:
    db_uri = LOCALDB

# -------------------- Groq API Key -------------------- #
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

if not api_key:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar.")
    st.stop()

# -------------------- Initialize Groq LLM -------------------- #
try:
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="Llama3-8b-8192",
        streaming=True
    )
except Exception as e:
    st.error(f"❌ Error initializing Groq LLM: {str(e)}")
    st.stop()

# -------------------- Database Configuration -------------------- #
@st.cache_resource(ttl=7200)
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    """Configure and return SQLDatabase instance."""
    if db_uri == LOCALDB:
        db_path = Path.cwd() / "student.db"
        if not db_path.exists():
            st.error("❌ 'student.db' not found in current directory.")
            st.stop()
        engine = create_engine(f"sqlite:///{db_path}")
        return SQLDatabase(engine)
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("⚠️ Please provide all MySQL connection details.")
            st.stop()
        connection_uri = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
        engine = create_engine(connection_uri)
        return SQLDatabase(engine)

# -------------------- Load Database -------------------- #
if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

# -------------------- Create LangChain SQL Agent -------------------- #
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# -------------------- Chat Interface -------------------- #
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "👋 Hi! How can I help you with your database today?"}]

# Clear chat option
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Chat history cleared. How can I help you now?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User query input
user_query = st.chat_input("Ask anything from your database...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        try:
            response = agent.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error processing query: {str(e)}")
