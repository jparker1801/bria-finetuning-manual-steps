import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def create_model_function(name, dataset_id, training_mode, description):
    url = "https://engine.prod.bria-api.com/v1/tailored-gen/models"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    # Fully automated training mode is standard
    payload = {
        "name": name,
        "dataset_id": dataset_id,
        "training_mode": training_mode,
        "description": description 
    }

    print(f"Attempting to start training for model: '{name}'")

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            model_id = result.get("id") or result.get("model_id")
            print(f"Model training initiated successfully! Model ID: {model_id}")
            return result
        else:
            print(f"Failed to create model. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None