import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def create_project_function(project_name, ip_name, ip_description, ip_medium, ip_type):
    # Base URL for creating projects as per tailored generation docs
    url = "https://engine.prod.bria-api.com/v1/tailored-gen/projects" 
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    payload = {
        "project_name": project_name,
        "ip_name": ip_name,
        "ip_description": ip_description,
        "ip_type": ip_type,
        "ip_medium": ip_medium
    }

    if project_name:
        print(f"Attempting to create project: {project_name}")

    try:
        response = requests.post(url, json=payload, headers=headers)

        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            project_id = result.get("id") or result.get("project_id")
            print(f"Project created successfully! Project ID: {project_id}")
            return result
        else:
            print(f"Failed to create project. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None