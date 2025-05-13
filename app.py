from flask import Flask, jsonify

app = Flask(__name__)

# In-memory list to simulate job database
jobs = []

@app.route("/")
def home():
    return "Welcome to DevOps Job Tracker"

@app.route("/add-job")
def add_job():
    jobs.append({"title": "DevOps Engineer", "status": "applied"})
    return f"{len(jobs)} job(s) added."

@app.route("/list-jobs")
def list_jobs():
    return jsonify({"jobs": jobs})

if __name__ == "__main__":
    # IMPORTANT: host="0.0.0.0" makes the app reachable from outside the container
    app.run(host="0.0.0.0", port=5000, debug=True)
