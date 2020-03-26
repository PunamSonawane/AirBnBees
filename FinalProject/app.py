from flask import (
    Flask,
    render_template,
    jsonify,
    json, 
    current_app as app,
    request,
    redirect)

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dash")
def dash():
    return render_template("dashboard.html")

@app.route("/model")
def model():
    return render_template("dashboard.html")

@app.route("/map")
def map():
    return render_template("dashboard.html")
if __name__ == "__main__":
    app.run(debug=True)