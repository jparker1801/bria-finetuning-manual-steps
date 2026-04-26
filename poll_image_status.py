import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
bria_api_key = os.getenv("BRIA_API_KEY")

def poll_image_status_function(request_id, output_filename):
    status_url = f"https://engine.prod.bria-api.com/v2/status/{request_id}"
    headers = {"api_token": bria_api_key}
    
    print(f"Polling for image completion. Request ID: {request_id}")
    
    while True:
        response = requests.get(status_url, headers=headers)
        
        try:
            result = response.json()
        except Exception:
            print("Error parsing status response:", response.text)
            time.sleep(5)
            continue

        if response.status_code == 200:
            current_status = result.get("status", "").lower()
            
            if current_status == "success" or "result" in result:
                print("\nImage generation complete! Attempting to download...")
                
                # --- Downloading Phase ---
                image_url = None
                if "result" in result:
                    if "urls" in result["result"] and len(result["result"]["urls"]) > 0:
                        image_url = result["result"]["urls"][0]
                    elif "image_url" in result["result"]:
                        image_url = result["result"]["image_url"]
                elif "urls" in result and len(result["urls"]) > 0:
                    image_url = result["urls"][0]
                
                if image_url:
                    # Create the local folder and set the save path
                    project_dir = os.path.dirname(os.path.abspath(__file__))
                    output_dir = os.path.join(project_dir, "generated_images")
                    os.makedirs(output_dir, exist_ok=True)
                    
                    save_path = os.path.join(output_dir, output_filename)
                    
                    # Download and save the image locally
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
                
            elif current_status in ["failed", "error"]:
                print("\nImage generation failed during processing.")
                print("Response:", result)
                return None
            else:
                print(f"Status: {current_status}... checking again in 5 seconds.")
                time.sleep(5)
        else:
            print(f"Failed to check status. Code: {response.status_code}")
            time.sleep(5)