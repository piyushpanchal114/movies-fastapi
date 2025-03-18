import os
import httpx
import uuid


CAST_SERVICE_HOST_URL = "http://localhost:8003/api/v1/casts/"
url = os.environ.get("CAST_SERVICE_HOST_URL") or CAST_SERVICE_HOST_URL


def is_cast_present(cast_id: uuid.UUID) -> bool:
    r = httpx.get(f"{url}{cast_id}")
    return r if r.status_code == 200 else False
