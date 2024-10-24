class QubiconError(Exception):
    """Base exception class for the Qubicon library."""
    pass

class AuthenticationError(QubiconError):
    """Exception raised for authentication errors."""
    pass

class APIRequestError(QubiconError):
    """Exception raised for API request errors."""
    pass

class NotFoundError(QubiconError):
    """Exception raised when a requested resource is not found."""
    pass

class ValidationError(QubiconError):
    """Exception raised for data validation errors."""
    pass
