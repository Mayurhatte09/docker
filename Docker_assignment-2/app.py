from flask import Flask
import argparse
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.environ.get("FLASK_PORT", 5000)))
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)

