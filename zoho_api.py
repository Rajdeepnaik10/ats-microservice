import requests
import os
# 🔑 Replace with your latest access token (expires ~1 hour)
ACCESS_TOKEN = os.environ.get("ZOHO_ACCESS_TOKEN")

# 🌍 Zoho Recruit API (India region)
BASE_URL = "https://recruit.zoho.in/recruit/v2"


# =========================
# 📌 COMMON HEADERS
# =========================
def get_headers():
    return {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }


# =========================
# 📌 GET JOBS
# =========================
def get_jobs():
    url = f"{BASE_URL}/JobOpenings"
    headers = get_headers()

    response = requests.get(url, headers=headers)

    print("\n--- GET JOBS DEBUG ---")
    print("STATUS:", response.status_code)

    # ✅ HANDLE 204 properly
    if response.status_code == 204:
        return {
            "success": True,
            "data": [],
            "message": "No jobs found in Zoho"
        }

    try:
        return {
            "success": True,
            "data": response.json()
        }
    except:
        return {
            "success": False,
            "error": "Invalid JSON response from Zoho",
            "raw": response.text
        }


# =========================
# 📌 GET CANDIDATES
# =========================
def get_candidates():
    url = f"{BASE_URL}/Candidates"
    headers = get_headers()

    try:
        response = requests.get(url, headers=headers)

        # Handle no data
        if response.status_code == 204:
            return {
                "success": True,
                "data": [],
                "message": "No candidates found"
            }

        # Normal response
        return {
            "success": True,
            "data": response.json()
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


# =========================
# 📌 CREATE CANDIDATE
# =========================
def create_candidate(data):
    url = f"{BASE_URL}/Candidates"
    headers = get_headers()

    payload = {
        "data": [data]
    }

    response = requests.post(url, headers=headers, json=payload)

    print("\n--- CREATE CANDIDATE DEBUG ---")
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text[:300])

    try:
        return {
            "success": True,
            "data": response.json()
        }
    except:
        return {
            "success": False,
            "error": "Invalid JSON response from Zoho",
            "raw": response.text
        }