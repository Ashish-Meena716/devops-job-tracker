from flask import Flask

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
    return {"jobs": jobs}

if __name__ == "__main__":
    app.run(debug=True)

