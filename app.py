
from flask import Flask, render_template

app = Flask(__name__)

devices = [
    {"name": "Router", "ip": "192.168.1.1", "status": "Online", "latency": 5},
    {"name": "Server", "ip": "192.168.1.2", "status": "Online", "latency": 12},
    {"name": "Laptop", "ip": "192.168.1.3", "status": "Online", "latency": 8},
    {"name": "Printer", "ip": "192.168.1.4", "status": "Offline", "latency": None}
]

@app.route("/")
def home():
    online = sum(d["status"] == "Online" for d in devices)
    return render_template(
        "index.html",
        devices=devices,
        total=len(devices),
        online=online,
        offline=len(devices) - online
    )

if __name__ == "__main__":
    app.run(debug=True)
