import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def create_dataset_function(project_id, dataset_name):
    # Base URL for datasets
    url = "https://engine.prod.bria-api.com/v1/tailored-gen/datasets"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    # Passing both the project ID to link it, and the name of the dataset
    payload = {
        "project_id": project_id,
        "name": dataset_name
    }

    print(f"Attempting to create dataset '{dataset_name}' for Project ID: {project_id}")

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            dataset_id = result.get("id") or result.get("dataset_id")
            print(f"Dataset created successfully! Dataset ID: {dataset_id}")
            return result
        else:
            print(f"Failed to create dataset. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None