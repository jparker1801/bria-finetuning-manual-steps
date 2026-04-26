import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def check_model_status_function(model_id):
    url = f"https://engine.prod.bria-api.com/v1/tailored-gen/models/{model_id}"
    headers = {"api_token": bria_api_key}

    print(f"Checking status for Model ID: {model_id}...")

    try:
        response = requests.get(url, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            status = result.get("status")
            print(f"Current Model Status: {status}")
            return status
        else:
            print(f"Failed to get model status. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None