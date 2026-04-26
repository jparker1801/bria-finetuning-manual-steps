import os

def run_setup():
    # 1. Create the .env file with a placeholder
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("BRIA_API_KEY=your_api_key_here\n")
        print("✅ Created .env file (Don't forget to add your key!)")
    else:
        print("ℹ️ .env file already exists.")

    # 2. Create the necessary project folders
    folders = ["dataset", "generated_images"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Created folder: {folder}")
        else:
            print(f"ℹ️ Folder already exists: {folder}")

    print("\n🚀 Setup complete! Add your training images to the 'dataset' folder and configure main1.py")

if __name__ == "__main__":
    run_setup()