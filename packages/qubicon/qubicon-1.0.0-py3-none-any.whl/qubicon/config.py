import os

class Config:
    def __init__(self, base_url, timeout=30):
        """
        Configuration class for Qubicon API interactions.

        :param base_url: Base URL of the Qubicon API (customer-specific).
        :param timeout: Request timeout in seconds.
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.token = None
        self.config_dir = os.path.expanduser('~/.qubicon')
        self.token_file = os.path.join(self.config_dir, 'token')

    def save_token(self, token):
        """Save the authentication token."""
        self.token = token
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        with open(self.token_file, 'w') as f:
            f.write(token)

    def load_token(self):
        """Load the authentication token."""
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as f:
                self.token = f.read().strip()
        return self.token

    def delete_token(self):
        """Delete the saved authentication token."""
        if os.path.exists(self.token_file):
            os.remove(self.token_file)
        self.token = None
