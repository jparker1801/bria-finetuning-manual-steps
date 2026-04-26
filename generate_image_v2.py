import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def generate_image_function_v2(model_id, prompt):
    url = "https://engine.prod.bria-api.com/v2/image/generate/tailored"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    payload = {
        "tailored_model_id": str(model_id),
        "prompt": prompt
    }

    print(f"Attempting to generate image (V2) with model ID: {model_id}")

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        
        if response.status_code == 202:
            request_id = result.get("request_id")
            print("\n" + "=" * 50)
            print(f"Generation job started successfully!")
            print(f"IMPORTANT: Copy this Request ID -> {request_id}")
            print("=" * 50)
            return request_id
            
        elif response.status_code in [200, 201]:
            print("Image generated synchronously!")
            return result
        else:
            print(f"Failed to start generation. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None