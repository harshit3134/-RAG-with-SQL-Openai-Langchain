import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

#conncetion to the database , change the password,user and db_name accordingly
db = SQLDatabase.from_uri(f"mysql+pymysql://root:password@localhost/db_name")

os.environ["OPENAI_API_KEY"] = "your key"

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

def get_answer(query):

    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    response=db_chain.run(query+"give me the response in a human manner")
    return response

get_answer("How many tables are there in the database?")
