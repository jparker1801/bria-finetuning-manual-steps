import os
import requests
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def generate_image_function(tailored_model_id, prompt, output_filename):
    url = "https://engine.prod.bria-api.com/v1/image/generate/tailored"
    headers = {"Content-Type": "application/json", "api_token": bria_api_key}
    
    payload = {
        "tailored_model_id": tailored_model_id,
        "prompt": prompt
    }

    print(f"Attempting to generate image with model ID: {tailored_model_id}")
    print(f"Prompt: '{prompt}'")

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error: Failed to Parse JSON Response:", response.text)
            return None

        if response.status_code in [200, 201]:
            print("Image generated successfully! Attempting to download...")
            
            
            image_url = None
            if "urls" in result:
                image_url = result["urls"][0]
            elif "result" in result and "urls" in result["result"]:
                image_url = result["result"]["urls"][0]
            
            if image_url:
                project_dir = os.path.dirname(os.path.abspath(__file__))
                output_dir = os.path.join(project_dir, "generated_images")
                os.makedirs(output_dir, exist_ok=True)
                
                save_path = os.path.join(output_dir, output_filename)
                
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    with open(save_path, "wb") as f:
                        f.write(image_response.content)
                    print(f"Image saved locally to: {save_path}")
                else:
                    print(f"Failed to download image. Status code: {image_response.status_code}")
            else:
                print("Could not locate image URL in the response payload:", result)

            return result
        else:
            print(f"Failed to generate image. Status code: {response.status_code}")
            print("Response:", result)
            return None

    except Exception as e:
        print("Error processing API response:", str(e))
        return None