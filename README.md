# ATS Microservice - Internship Task 2

## Overview

This project implements a simple **ATS (Applicant Tracking System) microservice** using **Serverless Framework and Python**.

The microservice simulates integration with the **Recruitee API** using a mock implementation.

It allows:

* Fetching available jobs
* Creating candidate applications
* Viewing applications for a specific job

---

## Tech Stack

* Python
* Serverless Framework
* AWS Lambda (simulated locally)
* serverless-offline plugin

---

## Project Structure

```
ats_microservice/
│
├── handler.py           # Lambda handlers (API endpoints)
├── mock_recruitee.py    # Mock Recruitee API
├── serverless.yml       # Serverless configuration
├── requirements.txt
└── README.md
```

---

## API Endpoints

### 1️⃣ Get Jobs

GET

```
/dev/jobs
```

Example Response

```
[
 { "id": "1", "title": "Backend Developer" },
 { "id": "2", "title": "Frontend Developer" }
]
```

---

### 2️⃣ Create Candidate

POST

```
/dev/candidates
```

Example Request

```
{
 "name": "Rajdeep",
 "email": "rajdeep@test.com",
 "phone": "9999999999",
 "resume_url": "link",
 "job_id": "1"
}
```

Example Response

```
{
 "id": "1",
 "candidate_name": "Rajdeep",
 "email": "rajdeep@test.com",
 "status": "APPLIED",
 "job_id": "1"
}
```

---

### 3️⃣ Get Applications

GET

```
/dev/applications?job_id=1
```

Example Response

```
[
 {
  "id": "1",
  "candidate_name": "Rajdeep",
  "email": "rajdeep@test.com",
  "status": "APPLIED",
  "job_id": "1"
 }
]
```

---

## Setup Instructions

### 1️⃣ Install dependencies

```
npm install
pip install -r requirements.txt
```

### 2️⃣ Run server

```
serverless offline
```

Server will start at:

```
http://localhost:3000
```

---

## Testing APIs

Open browser or use Postman.

Examples:

```
GET http://localhost:3000/dev/jobs
```

```
GET http://localhost:3000/dev/applications?job_id=1
```

```
POST http://localhost:3000/dev/candidates
```

---

## Author

Rajdeep Naik
