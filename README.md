# ATS Microservice (Zoho Recruit Integration)

## 🚀 Overview

This project is a serverless microservice that integrates with Zoho Recruit API to fetch job openings and candidate data.

## 🛠 Tech Stack

* Python
* Serverless Framework
* Zoho Recruit API
* AWS Lambda (offline)

## ⚙️ Features

* Fetch job openings from Zoho
* Fetch candidate details
* OAuth 2.0 integration
* Error handling (empty data, invalid token)
* Modular architecture (handler + service layer)

## 📡 API Endpoints

### Get Jobs

GET /dev/jobs

### Get Candidates

GET /dev/candidates

## 🧠 Architecture

* `handler.py` → Lambda handlers
* `zoho_api.py` → External API service layer
* `mock_recruitee.py` → Initial mock API (for development)

## 🔐 Environment Variables

```
ZOHO_ACCESS_TOKEN=your_access_token
```

## ▶️ Run Locally

```
npm install
pip install -r requirements.txt
serverless offline
```

## 🎯 Future Improvements

* Auto refresh token
* Deployment on AWS
* Add POST endpoints (create candidate)

## 👨‍💻 Author

Rajdeep Naik
