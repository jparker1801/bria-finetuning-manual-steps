import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def start_training_function(model_id):
    url = f"https://engine.prod.bria-api.com/v1/tailored-gen/models/{model_id}/start_training"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}

    print(f"Attempting to start training for Model ID: {model_id}")

    try:
        # We pass an empty json object because 'fully_automated' mode uses default parameters
        response = requests.post(url, json={}, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            print(f"Training successfully started for Model ID: {model_id}!")
            return result
        else:
            print(f"Failed to start training. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None