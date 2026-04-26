import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def complete_dataset_function(dataset_id):
    url = f"https://engine.prod.bria-api.com/v1/tailored-gen/datasets/{dataset_id}"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    # We must explicitly set the status to 'completed'
    payload = {
        "status": "Completed"
    }

    print(f"Attempting to mark Dataset ID: {dataset_id} as 'completed'")

    try:
        response = requests.put(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            print(f"Dataset {dataset_id} marked as completed successfully!")
            return result
        else:
            print(f"Failed to complete dataset. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None