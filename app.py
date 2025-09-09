from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, MLOps on Azure!"

@app.route("/hello")
def hello():
    return "Hello from Azure!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/broken")
def broken():  # <-- fixed
    return "This works now!"

def broken_style():
  return  "Extra spaces here"
