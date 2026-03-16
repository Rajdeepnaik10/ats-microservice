import json
import os

DATA_FILE = "applications.json"


jobs = [
    {"id": "1", "title": "Backend Developer"},
    {"id": "2", "title": "Frontend Developer"}
]


def load_applications():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_applications(applications):
    with open(DATA_FILE, "w") as f:
        json.dump(applications, f)


def get_jobs():
    return jobs


def create_candidate(data):
    applications = load_applications()

    application = {
        "id": str(len(applications) + 1),
        "candidate_name": data["name"],
        "email": data["email"],
        "status": "APPLIED",
        "job_id": data["job_id"]
    }

    applications.append(application)
    save_applications(applications)

    return application


def get_applications(job_id):
    applications = load_applications()

    filtered = [
        app for app in applications
        if app["job_id"] == str(job_id)
    ]

    return filtered