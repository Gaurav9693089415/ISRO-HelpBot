# isro_helpbot/cli.py

import subprocess
import os

def main():
    app_path = os.path.join(os.path.dirname(__file__), "../ui/streamlit_app.py")
    subprocess.run(["streamlit", "run", app_path])
