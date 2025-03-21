import requests
from typing import Optional
import os

BASE_API_URL = "http://127.0.0.1:7860"


def get_askai(question, profile): 
  
  TWEAKS = {
    "TextInput-3vZ2Z": {
      "input_value": question
     },
    "TextInput-IQI7V": {
    "input_value": profile
    },
    }
  return run_flow(question, endpoint = "askai",langflow_id= "4d835698-5b3a-42aa-be1b-15e65fc2b676",  tweaks=TWEAKS)

def get_macros(profile, goals):
  TWEAKS = {
    "TextInput-g8OEn": {
      "input_value": goals
    }, 
    "TextInput-Dfbwd": {
      "input_value": profile
    },
    }
  return run_flow("", endpoint = "macros",langflow_id= "f9586dee-c724-486d-8589-e3f7d4f64b8e" , tweaks=TWEAKS)

def run_flow(message: str,
  endpoint: str,
  langflow_id: str, 
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"

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
    response = requests.post(api_url, json=payload, headers=headers, timeout=60)
   
    return response.json()["outputs"][0]["outputs"][0]['results']["text"]["data"]["text"]
 
res = get_macros("name: kennedy age: 27: wieght: 80kg 175cm ", "I want to losse stomach fat")
print(res)
print("\n")
res = get_askai("how many fats should i burn", "name: kennedy age: 27: wieght: 80kg 175cm ")
print(res)

