import requests
from .exceptions import AuthenticationError, APIRequestError
from .logger import get_logger

logger = get_logger(__name__)

def make_request(method, url, headers=None, json=None, data=None, params=None, timeout=30):
    try:
        if method == 'POST' or method == 'PUT':
            if json:
                response = requests.request(
                    method,
                    url,
                    headers=headers,
                    json=json,  # Send JSON payload
                    params=params,
                    timeout=timeout
                )
            else:
                response = requests.request(
                    method,
                    url,
                    headers=headers,
                    data=data,  # Send form data or other payload
                    params=params,
                    timeout=timeout
                )
        else:
            response = requests.request(
                method,
                url,
                headers=headers,
                params=params,
                timeout=timeout
            )

        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            logger.error("Authentication error: Unauthorized access.")
            raise AuthenticationError("Unauthorized access.")
        else:
            logger.error(f"HTTP error occurred: {e}")
            raise APIRequestError(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception: {e}")
        raise APIRequestError(f"Request exception: {e}")
