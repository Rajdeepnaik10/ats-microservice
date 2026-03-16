import json
from mock_recruitee import get_jobs, create_candidate, get_applications


def jobs(event, context):
    """
    GET /jobs
    Returns list of jobs
    """

    data = get_jobs()

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }


def candidates(event, context):
    """
    POST /candidates
    Creates a candidate application
    """

    try:
        body = json.loads(event.get("body", "{}"))

        result = create_candidate(body)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e)
            })
        }


def applications(event, context):
    """
    GET /applications?job_id=
    Returns applications for a job
    """

    params = event.get("queryStringParameters") or {}
    job_id = params.get("job_id")

    if not job_id:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "job_id query parameter required"
            })
        }

    try:
        result = get_applications(job_id)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }