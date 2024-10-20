# exceptions.py

class CustomError(Exception):
    """Base class for all custom exceptions in the project."""
    pass


class MultiQueryGenerationError(CustomError):
    """Raised when the Multiple queries are not generated."""

    def __init__(self, message="First Generate Multiple Queries before doing any other operation."):
        self.message = message
        super().__init__(self.message)


class MultiQueryNotImplementedError(CustomError):
    """Raised when the Multiple queries are not generated."""

    def __init__(self, message="First Generate Multiple Queries before doing any other operation."):
        self.message = message
        super().__init__(self.message)


class MissingResourceError(CustomError):
    """Raised when a required resource is not found."""

    def __init__(self, resource_name):
        self.message = f"The {resource_name}' was not found."
        super().__init__(self.message)


class ResponseGenerationError(CustomError):
    """Raised when the error occurs during response generation."""

    def __init__(self, message="Response generation failed."):
        self.message = message
        super().__init__(self.message)


class DataProcessingError(CustomError):
    """Raised when there is an error in data processing."""

    def __init__(self, message="An error occurred while processing data."):
        self.message = message
        super().__init__(self.message)


class ConfigurationError(CustomError):
    """Raised when there is an error in configuration."""

    def __init__(self, message="Configuration is invalid."):
        self.message = message
        super().__init__(self.message)


class TimeoutError(CustomError):
    """Raised when an operation times out."""

    def __init__(self, message="The operation timed out."):
        self.message = message
        super().__init__(self.message)
