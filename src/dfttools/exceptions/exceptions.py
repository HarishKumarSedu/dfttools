class DFTError(Exception):
    """Base exception for all DFT-related errors."""

class InvalidValueError(DFTError):
    """Raised when an invalid enum value is used."""

class HardwareError(DFTError):
    """Raised for hardware communication failures."""
