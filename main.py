import subprocess
import sys

if __name__ == "__main__":
    try:
        subprocess.run(["streamlit", "run", "ui/dashboard.py"])
    except KeyboardInterrupt:
        sys.exit(0)