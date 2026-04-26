# Bria AI Fine-Tuning: Manual Workflow

This repository contains a step-by-step, manual Python workflow for fine-tuning a custom AI model using the [Bria AI Tailored Generation API](https://docs.bria.ai/tailored-generation). 

Because AI model training takes time and requires strict sequential steps, this project is designed to be executed **one section at a time** by commenting and uncommenting specific blocks in the `main1.py` file.

---

## 🚀 Quick Start

1. **Clone the repo:**
```bash
git clone [https://github.com/jparker1801/bria-finetuning-manual-steps.git](https://github.com/jparker1801/bria-finetuning-manual-steps.git)
cd bria-finetuning-manual-steps
```

## 2. **Install Required Librarie:** 
```bash
pip install -r requirements.txt
```

3. **Run the setup.py:**
```bash
python3 setup.py
```

4. **Step-by-Step Guide:**
Step 1: Create a Project
Uncomment Step 1. Define your project characteristics (name, IP type, medium). Run the script to generate your project_id. Update the project_id variable in Step 2A.

Step 2: Dataset Management
Step 2A: Create the Dataset Container - Uses your project_id to create an empty dataset. This returns a dataset_id.

Step 2B: Upload Images - Updates the script with your new dataset_id. This step loops through your local dataset/ folder and uploads all images to Bria via Base64 encoding.

Step 3: Model Creation & Training
Step 3A: Create the Model - Registers the model container based on your dataset. Returns a model_id.

Step 3B: Set Status to Completed - Crucial step. Locks the dataset so Bria knows no more images are coming.

Step 3C: Start Training - Fires up the GPUs to begin the training process.

Step 3D: Check Status (Polling) - A background loop that checks your model's status every 10 minutes. Leave this running! It will alert you when the status changes to Active or Completed.

Step 4: Generate a Tailored Image
Once training is complete, you can generate images using your custom model!

Step 4A: Start Image Generation (V2) - Send a prompt to your fine-tuned model. Bria's V2 API processes this asynchronously and returns a request_id.

Step 4B: Poll and Download - Paste the request_id into this section. The script will poll Bria until the image is ready, automatically download it, and save it to a new local folder called generated_images/.
