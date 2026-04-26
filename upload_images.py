import os
import requests
from dotenv import load_dotenv
from image_to_base64 import image_to_base64  # Importing from your existing module

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def upload_image_function(dataset_id, image_path):
    url = f"https://engine.prod.bria-api.com/v1/tailored-gen/datasets/{dataset_id}/images"
    
    # We bring back the JSON Content-Type header
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}

    filename = os.path.basename(image_path)
    print(f"Attempting to upload: {filename}")

    try:
        # Convert the image file to a Base64 string using your imported function
        base64_string = image_to_base64(image_path)
        
        # Send the base64 string in the JSON payload
        payload = {
            "file": base64_string,
            "filename": filename 
        }

        response = requests.post(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            print(f"Successfully uploaded {filename}!")
            return result
        else:
            print(f"Failed to upload {filename}. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing file upload:", str(e))
        return None