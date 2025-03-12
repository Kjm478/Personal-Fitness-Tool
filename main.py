import requests
from typing import Optional
import os

BASE_API_URL = "http://127.0.0.1:7860"


def get_askai(question): 
  
  TWEAKS = {
    "TextInput-3vZ2Z": {
      "input_value": question
     },
    }
  return run_flow("", endpoint = "askai",langflow_id= "4d835698-5b3a-42aa-be1b-15e65fc2b676",  tweaks=TWEAKS)

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
    print(response.json())
    print(response.status_code)
    print(response.text)
    return response.json()["outputs"][0]["outputs"][0]['results']["text"]["data"]["text"]
 

print("\n")
res = get_macros("What is 300 + 200", "I want to be a data scientist")
print(res)

