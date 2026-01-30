from flask import Flask

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/flask"

@app.route("/")
def hello():
    return "Hello from Flask at /flask 🎯"
