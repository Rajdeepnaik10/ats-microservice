import json
from zoho_api import get_jobs, get_candidates, create_candidate


# GET /dev/jobs
def get_jobs_handler(event, context):
    try:
        jobs = get_jobs()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "data": jobs
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }


# GET /dev/candidates
def get_candidates_handler(event, context):
    try:
        candidates = get_candidates()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "data": candidates
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }


# POST /dev/candidates
def create_candidate_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        name = body.get("name")
        email = body.get("email")

        if not name or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "success": False,
                    "error": "Name and Email are required"
                })
            }

        result = create_candidate(name, email)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "data": result
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }