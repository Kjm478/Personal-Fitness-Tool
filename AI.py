import requests
from typing import Optional
import os
import json 
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = "http://127.0.0.1:7861"

def dict_to_string(obj, level = 0):
  strings = []
  indent = "  " * level #indentation for nested levels
  
  if isinstance(obj, dict):
    for key, value in obj.items():
      if isinstance(value, dict):
        strings.append(f"{indent}{key}:")
        strings.extend(dict_to_string(value, level + 1))
      else:
        strings.append(f"{indent}{key}: {value}")
        
  elif isinstance(obj, list):
    for idx, item in enumerate(obj):
      nested = dict_to_string(item, level + 1)
      strings.append(f"{indent}item{idx+ 1}:{nested}")
  else:
    strings.append(f"{indent}{obj}")
  return ",".join(strings)


def get_askai(question, profile): 
  
  TWEAKS = {
    "TextInput-3vZ2Z": {
      "input_value": question
     },
    "TextInput-IQI7V": {
    "input_value": dict_to_string(profile)
    },
    }
  return run_flow(question, endpoint = "askai",langflow_id= "4d835698-5b3a-42aa-be1b-15e65fc2b676",  tweaks=TWEAKS)

def get_macros(profile, goals):
  TWEAKS = {
    "TextInput-g8OEn": {
      "input_value": ",".join(goals)
    }, 
    "TextInput-Dfbwd": {
      "input_value": dict_to_string(profile)
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
    response = requests.post(api_url, json=payload, headers=headers)
    
    if endpoint == "askai":
        return (response.json()["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"])
   
    return json.loads(response.json()["outputs"][0]["outputs"][0]['results']["text"]["data"]["text"])

if __name__ == "__main__":
  print(get_askai("create a leg day routine for me", {"calories": 2000, "protein": 100, "carbs": 200, "fat": 50}))