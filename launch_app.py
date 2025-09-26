#!/usr/bin/env python3
"""
Launch script for the AI Content Creation Studio
================================================

This script launches the new Streamlit application with proper configuration.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Launch the Streamlit application."""
    
    print("🚀 Starting AI Content Creation Studio...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("new_streamlit_app.py").exists():
        print("❌ Error: new_streamlit_app.py not found!")
        print("Please run this script from the project directory.")
        sys.exit(1)
    
    # Check if virtual environment exists
    if not Path("venv").exists():
        print("❌ Error: Virtual environment not found!")
        print("Please create a virtual environment first:")
        print("python -m venv venv")
        print("source venv/bin/activate")
        print("pip install -r requirements_new.txt")
        sys.exit(1)
    
    # Launch Streamlit
    try:
        print("🌐 Launching Streamlit application...")
        print("📱 The app will open in your browser at: http://localhost:8501")
        print("🛑 Press Ctrl+C to stop the application")
        print("=" * 50)
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "new_streamlit_app.py",
            "--server.headless", "true",
            "--server.port", "8501"
        ])
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"❌ Error launching application: {e}")

if __name__ == "__main__":
    main()
