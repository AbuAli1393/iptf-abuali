from flask import Flask, render_template, request, send_file
import json
from src.iptf import IPTFEngine

app = Flask(__name__)
results = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target")
        mode = request.form.get("mode", "full")

        engine = IPTFEngine(target, mode)
        engine.run()
        engine.generate_report("report.json")
        results[target] = json.load(open("report.json"))

        return render_template("results.html", target=target, results=results[target])

    return render_template("index.html")

@app.route("/download")
def download_report():
    return send_file("report.json", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
