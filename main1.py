import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from create_project import create_project_function
from create_dataset import create_dataset_function
from upload_images import upload_image_function
from create_model import create_model_function
from complete_dataset import complete_dataset_function
from start_training import start_training_function
from check_model_status import check_model_status_function
from generate_image import generate_image_function
from generate_image_v2 import generate_image_function_v2
from poll_image_status import poll_image_status_function

# --------------------------------------------------------------------------------------------------
# Start Main Script
# --------------------------------------------------------------------------------------------------

load_dotenv()
api_key = os.getenv("BRIA_API_KEY")

# --------------------------------------------------------------------------------------------------
# Step 1: Create a Project
# --------------------------------------------------------------------------------------------------

# Define your project characteristics
# project_name = "FIBO TG Test"
# ip_name = "Adventure Series Characters"
# ip_description = "A set of adventure game characters with unique personalities"
# ip_medium = "illustration"
# ip_type = "defined_character" # Options: multi_object_set, defined_character, stylized_scene


# print("Initializing Step 1: Project Creation...")
# project_data = create_project_function(project_name, ip_name, ip_description, ip_medium, ip_type)

# if project_data:
#     print("Project data returned:", project_data)
#     print("Step 1 Complete.")

# --------------------------------------------------------------------------------------------------
# Step 2A: Create the Dataset Container
# --------------------------------------------------------------------------------------------------
# We will create the empty dataset first, confirm the ID, and then tackle the image upload loop!

# project_id = 13246 
# dataset_name = "Dragon_Images"

# print("Initializing Step 2: Dataset Creation...")
# dataset_data = create_dataset_function(project_id, dataset_name)

# if dataset_data:
#     print("Dataset data returned:", dataset_data)
#     print("Step 2 Complete. Ready to upload images!")

# --------------------------------------------------------------------------------------------------
# Step 2B: Upload Images to the Dataset
# --------------------------------------------------------------------------------------------------

# project_id = 13246 
# dataset_id = 15861 

# project_dir = os.path.dirname(os.path.abspath(__file__))
# dataset_dir = os.path.join(project_dir, "dataset")

# print("Initializing Step 2b: Image Upload...")

# # Check if the "dataset" folder actually exists
# if not os.path.exists(dataset_dir):
#     print(f"Error: The folder '{dataset_dir}' does not exist. Please create it and add images.")
# else:
#     # Valid extensions to look for
#     valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    
#     # Loop through all files in the "dataset" folder
#     for filename in sorted(os.listdir(dataset_dir)):
#         if filename.lower().endswith(valid_extensions):
#             image_path = os.path.join(dataset_dir, filename)
            
#             upload_data = upload_image_function(dataset_id, image_path)
            
#             if upload_data:
#                 print(f"Upload data returned for {filename}:", upload_data)
#                 print("-" * 50)
                
#     print("Step 2b Complete. Finished processing folder.")

# --------------------------------------------------------------------------------------------------
# Step 3A: Create the Model
# --------------------------------------------------------------------------------------------------

# project_id = 13246 
# name = "Dragon_Fine_Tuned_Model"
# dataset_id = 15861 
# training_mode = "fully_automated"
# description = "A model trained on Lora character illustrations"

# print("Initializing Step 3: Model Creation & Training...")
# model_data = create_model_function(name, dataset_id, training_mode, description)

# if model_data:
#     print("Model data returned:", model_data)
#     print("Step 3 Complete. The model has been created!")

# --------------------------------------------------------------------------------------------------
# Step 3B: Set Model Status to Completed
# --------------------------------------------------------------------------------------------------

# dataset_id = 15861 

# print("Initializing Step 3a.5: Marking Dataset as Completed...")
# complete_data = complete_dataset_function(dataset_id)

# if complete_data:
#     print("Dataset complete data returned:", complete_data)
#     print("-" * 50)

# --------------------------------------------------------------------------------------------------
# Step 3C: Start Training the Model
# --------------------------------------------------------------------------------------------------

# model_id = 13411 

# print("Initializing Step 3b: Starting Model Training...")
# start_data = start_training_function(model_id)

# if start_data:
#     print("Start training data returned:", start_data)
#     print("Step 3b Complete. The model is now training!")

# --------------------------------------------------------------------------------------------------
# Step 3D: Check Model Status
# --------------------------------------------------------------------------------------------------

# model_id = 13411 

# print("Initializing Step 3c: Checking Model Status...")
# current_status = check_model_status_function(model_id)

# print("-" * 50)
# if current_status and current_status.lower() in ["active", "completed", "ready"]:
#     print("Your model is ready! You can now uncomment and run Step 4 (Generate Image).")
# else:
#     print(f"Model is currently: {current_status}. Please wait a bit longer before generating.")

# --------------------------------------------------------------------------------------------------
# Step 3D: Automate Status Checking (Polling)
# --------------------------------------------------------------------------------------------------

model_id = 13411 
#Change back to 13411
sleep_minutes = 10 # Change this to 10 or 15 as you prefer
sleep_seconds = sleep_minutes * 60

print(f"Initializing Step 3c: Automating Model Status Check...")
print(f"Polling every {sleep_minutes} minutes. Feel free to leave this running in the background!")
print("-" * 50)

while True:
    current_status = check_model_status_function(model_id)
    
    if current_status and current_status.lower() in ["active", "completed", "ready"]:
        print("\n" + "=" * 50)
        print("The model has finished training! Moving to generation...")
        print("=" * 50)
        break # Exit the loop and proceed to generation
    
    elif current_status and current_status.lower() in ["failed", "error"]:
        print("\nModel training failed! Please check the Bria web UI for more details.")
        exit() # Stop the script entirely
        
    else:
        # Calculate the exact time of the next check
        next_check = datetime.now() + timedelta(seconds=sleep_seconds)
        formatted_time = next_check.strftime("%I:%M:%S %p") # Formats as HH:MM:SS AM/PM
        
        print(f"Model is currently: {current_status}.")
        print(f"Sleeping for {sleep_minutes} minutes. Next check will occur at: {formatted_time}")
        print("-" * 50)
        
        time.sleep(sleep_seconds)

# --------------------------------------------------------------------------------------------------
# Step 4: Generate a Tailored Image /v1
# --------------------------------------------------------------------------------------------------

# model_id = 13411
# prompt = "An illustration of a character named Adventure Series Dragon Characters, A set of adventure game characters with unique personalities, a fierce dragon flying over a futuristic city at night, neon lights illuminating its scales, cyberpunk style"
# output_filename = "cyberpunk_dragon.jpg"

# print("\nInitializing Step 4: Image Generation...")
# generation_data = generate_image_function(model_id, prompt, output_filename)

# if generation_data:
#     print("-" * 50)
#     print("Generation complete! Check your 'generated_images' folder.")
#     print("Full API Response:", generation_data)

# --------------------------------------------------------------------------------------------------
# Step 4: Generate a Tailored Image /v2
# --------------------------------------------------------------------------------------------------

# model_id = 13412
# prompt = "An illustration of a character named Adventure Series Dragon Characters, A set of adventure game characters with unique personalities, a fierce dragon flying over a futuristic city at night, neon lights illuminating its scales, cyberpunk style"
# output_filename = "cyberpunk_dragon.jpg"

# print("\nInitializing Step 4: Image Generation...")
# generation_data = generate_image_function_v2(model_id, prompt)

# if generation_data:
#     print("-" * 50)
#     print("Generation complete! Check your 'generated_images' folder.")
#     print("Full API Response:", generation_data)

# --------------------------------------------------------------------------------------------------
# Step 4B: Poll and Download (Paste the ID here and run this step)
# --------------------------------------------------------------------------------------------------

# manual_request_id = "1a99cba8e28e41ba899cfcb68ff68454"
# output_filename = "cyberpunk_dragon.jpg"

# print("\nInitializing Step 4B: Polling and Downloading...")
# final_data = poll_image_status_function(manual_request_id, output_filename)

# if final_data:
#     print("-" * 50)
#     print("Workflow fully complete!")