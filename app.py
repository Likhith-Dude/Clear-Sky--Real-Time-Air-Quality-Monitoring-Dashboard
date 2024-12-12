from flask import Flask, render_template, jsonify, send_file
import random
import time
import csv

app = Flask(__name__)

# Simulated real-time data
def generate_data():
    return {
        "PM2.5": random.randint(10, 200),
        "PM10": random.randint(50, 300),
        "CO2": random.randint(400, 800),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

data_store = [generate_data() for _ in range(10)]

@app.route("/")
def home():
    latest_data = data_store[-1]
    return render_template("dashboard.html", data=latest_data, history=data_store)

@app.route("/data")
def data():
    new_data = generate_data()
    data_store.append(new_data)
    return jsonify(new_data)

@app.route("/download")
def download():
    file_path = "air_quality_data.csv"
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["timestamp", "PM2.5", "PM10", "CO2"])
        writer.writeheader()
        writer.writerows(data_store)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)