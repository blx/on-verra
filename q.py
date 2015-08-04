import psutil as ps

from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter("b2m")
def b2m(b):
    """bytes 2 mebibytes"""
    return b / 1024 / 1024

@app.route("/")
def index():
    return render_template("index.html", m=ps.virtual_memory(), c=ps.cpu_percent(interval=0.4))

if __name__ == "__main__":
    app.run(debug=True)