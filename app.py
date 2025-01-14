import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how')
def hello():
    return 'I am good, how about you?'

@app.route('/health')
def health():
    return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
