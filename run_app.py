"""
AquaShield AI - 1-Click Python Launcher
Installs dependencies if missing, starts the server, and opens the browser.
"""
import sys
import os
import subprocess
import webbrowser
import time

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    
    print("=" * 60)
    print("  🌊 AQUASHIELD AI - COASTAL DISASTER INTELLIGENCE PLATFORM")
    print("=" * 60)
    print("\n[1/3] Checking dependencies...")
    
    try:
        import fastapi
        import uvicorn
    except ImportError:
        print("  -> Installing required packages (fastapi, uvicorn)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "pydantic", "python-multipart"])
        print("  -> Installation complete!")

    print("\n[2/3] Preparing AquaShield AI Server...")
    server_port = 8000
    app_url = f"http://127.0.0.1:{server_port}"
    
    import threading
    def open_browser():
        time.sleep(1.5)
        print(f"\n[3/3] Opening browser at {app_url} ...")
        webbrowser.open(app_url)
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    print(f"\n🚀 AquaShield AI Live at: {app_url}")
    print("💡 Press Ctrl+C in this terminal to stop the server anytime.\n")
    
    import uvicorn
    from backend.app.main import app
    uvicorn.run(app, host="127.0.0.1", port=server_port, log_level="info")

if __name__ == "__main__":
    main()
