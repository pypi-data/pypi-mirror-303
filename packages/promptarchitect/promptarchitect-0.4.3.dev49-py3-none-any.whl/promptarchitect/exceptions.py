"""Module containing custom exception classes for the promptarchitect package."""


class PromptArchitectError(Exception):
    """Base class for all custom exceptions in the promptarchitect package."""

    pass


class PromptValidationError(PromptArchitectError):
    """Exception raised for validation errors in the promptarchitect package."""

    pass


class PromptConfigurationError(PromptArchitectError):
    """Exception raised for configuration errors in the promptarchitect package."""

    pass


class PromptProcessingError(PromptArchitectError):
    """Exception raised for processing errors in the promptarchitect package."""

    pass
