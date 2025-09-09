from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, MLOps on Azure!"

@app.route("/hello")
def hello():
    return "Hello from Azure!"
