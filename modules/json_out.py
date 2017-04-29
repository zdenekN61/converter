"""Format of a json ouput"""

__all__ = ["json_out"]

# Output format.
def json_out():
    """City format

    Example:
    {   
        "input": {
            "amount": 0.9,
            "currency": "CNY"
        },
        "output": {
            "AUD": 0.20,
            ...
        }
    }
    """
    currency = {"input": {"amount": 0, "currency": ""}, "output": {}}
    return currency
