import os
import subprocess

def launch_app():
    subprocess.run(["streamlit", "run", "ui/streamlit_app.py"])
