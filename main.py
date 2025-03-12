from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
from typing import Optional
import os

BASE_API_URL = "https://api.langflow.astra.datastax.com"
APPLICATION_TOKEN = os.getenv("APPLICATION_TOKEN")


load_dotenv()

def ask_ai(question):
  TWEAKS = {
    "TextInput-fanPK": {
      "input_value": question
    },
    "TextInput-CXuEG": {
      "input_value": "profile"
    },
    }
  result = run_flow_from_json(flow = "AskAI.json", 
                              input_type= "message", 
                              fallback_to_env_vars=True,
                              tweaks=TWEAKS)
  
  return result[0].outputs[0].results["text"].data["text"]

def get_askai(question): 
  
  LANGFLOW_ID = "24b19386-5be7-48db-97af-c55ad05efe6b"
  ENDPOINT = "askai" # The endpoint name of the flow
  
  TWEAKS = {
    "TextInput-fanPK": {
      "input_value": question
    },
    "TextInput-CXuEG": {
      "input_value": "profile"
    },
    }
  return run_flow("", endpoint = ENDPOINT,langflow_id= LANGFLOW_ID,  tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def get_macros(profile, goals):
  TWEAKS = {
    "TextInput-3YLwx": {
      "input_value": goals
    }, 
    "TextInput-niwMA": {
      "input_value": profile
    },
    }
  return run_flow("", endpoint = "macros",langflow_id= "24b19386-5be7-48db-97af-c55ad05efe6b",  tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  endpoint: str,
  langflow_id: str, 
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{langflow_id}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
  
    return response.json()["outputs"][0]["outputs"][0]['results']["text"]["data"]["text"]




