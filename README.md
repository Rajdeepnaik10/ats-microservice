# ATS Microservice (Zoho Recruit Integration)

## 🚀 Overview

This project is a serverless microservice that integrates with Zoho Recruit API to fetch job openings and candidate data.

## Tech Stack
- Python
- Serverless Framework
- Zoho Recruit API

## Features
- Fetch Jobs from Zoho Recruit
- Fetch Candidates
- OAuth Token Handling
- Serverless Architecture

## API Endpoints
- GET /jobs
- GET /candidates


## 🧠 Architecture

* `handler.py` → Lambda handlers
* `zoho_api.py` → External API service layer


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

* ## Notes
- Uses Zoho OAuth access token

## 👨‍💻 Author

Rajdeep Naik
