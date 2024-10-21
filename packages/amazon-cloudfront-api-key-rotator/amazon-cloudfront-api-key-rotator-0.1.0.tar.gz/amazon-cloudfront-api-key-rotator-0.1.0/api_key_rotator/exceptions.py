"""
exceptions.py: This module defines custom exceptions for the CloudFront API key rotation process.
"""

class OriginTestFailedException(Exception):
    """
    Exception raised when the test of the origin using a new API key fails.
    """
