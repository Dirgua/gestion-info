import sys
import os

# Add the parent directory to the sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.menu import run

if __name__ == "__main__":
    run()
