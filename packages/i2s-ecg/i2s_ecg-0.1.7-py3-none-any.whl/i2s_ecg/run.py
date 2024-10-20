#run.py
import subprocess
import os

def run_app():
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current directory: {current_dir}")
    # Build the full path to app.py
    app_path = os.path.join(current_dir, 'app.py')
    
    # Ensure the app.py file exists
    if not os.path.exists(app_path):
        print(f"Error: {app_path} does not exist.")
        return
    
    # Use subprocess.run to run the streamlit run app.py command
    subprocess.run(["streamlit", "run", app_path,"--server.enableXsrfProtection=false"])

if __name__ == "__main__":
    run_app()