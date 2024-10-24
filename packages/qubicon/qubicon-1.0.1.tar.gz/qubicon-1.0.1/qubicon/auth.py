from .utils import make_request
from .exceptions import AuthenticationError
from .logger import get_logger

logger = get_logger(__name__)

def authenticate(config, username, password):
    """
    Authenticate with the Qubicon API and store the token in the config.

    :param config: Config object.
    :param username: User's username.
    :param password: User's password.
    :raises AuthenticationError: If authentication fails.
    """
    login_endpoint = '/api/login'
    url = f"{config.base_url}{login_endpoint}"
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/json'}

    logger.info("Attempting to authenticate with the Qubicon API...")
    response = make_request('POST', url, headers=headers, json=data, timeout=config.timeout)

    token = response.get('normal', {}).get('token')
    if token:
        config.save_token(token)
        logger.info("Authentication successful.")
    else:
        logger.error("Authentication failed.")
        raise AuthenticationError("Invalid credentials provided.")
