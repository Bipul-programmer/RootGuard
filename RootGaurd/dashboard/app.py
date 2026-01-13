from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "RootGuard Security Dashboard Active"

def run_dashboard():
    """Run the Flask dashboard. Call this from main.py in a separate thread."""
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)

if __name__ == "__main__":
    run_dashboard()