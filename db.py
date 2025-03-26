from dotenv import load_dotenv
from astrapy import DataAPIClient
import streamlit as st 
import os 


load_dotenv()

endpoint = os.getenv("endpoint_astra")
token = os.getenv("astra_db_token")

@st.cache_resource
def get_db():
    client = DataAPIClient(token)
    db = client.get_database_by_api_endpoint(endpoint)
    return db

db = get_db()
collection_names = ["personal_data", "notes"]

for name in collection_names:
    try:
       db.create_collection(name)
    except:
       pass
        
personal_data_collection = db.get_collection("personal_data")
notes_collection = db.get_collection("notes")

p