# Binlist Python Library

A Python Wrapper for BIN lookup using the Binlist API.

## Installation

You can install the package using pip:

```bash
pip install pybinlist
```

## Features

- Retrieve BIN information such as scheme, type, brand, prepaid status, country details, and bank name.
- Support for proxy requests to bypass restrictions (optional).
- Custom exception handling for better error management.

## Usage

Here’s how to use the Binlist Python library in your projects:

### Basic Usage

1. **Import the Library**: Import the necessary classes from the library.

```python
from binlist import BIN_Lookup, RateLimitExceededError, BINLookupError
```

2. **Create a BIN Lookup Instance**: Initialize the `BIN_Lookup` class with the desired BIN.

```python
api = BIN_Lookup()
```

3. **Fetch BIN Information**: Use the `fetch` method to retrieve information for a specific BIN. The `proxy` parameter is optional but can help bypass rate limits.

```python
try:
    info = api.fetch(bin='531462', proxy='http://your-proxy:port/')  # Proxy is optional
    print(f"Country: {info.country.name}, Bank: {info.bank.name}")
except (RateLimitExceededError, BINLookupError) as e:
    print(e)
```

### Handling Exceptions

The library provides custom exceptions to handle errors gracefully.

```python
try:
    info = api.fetch(bin='531462')
except RateLimitExceededError as e:
    print(f"Error: {e.message}")
except BINLookupError as e:
    print(f"Error: {e.message}")
```

### Fetching Raw JSON Response

If you prefer to get the raw JSON response, you can use the `fetch_json` method:

```python
try:
    raw_data = api.fetch_json(bin='531462')
    print(raw_data)
except (RateLimitExceededError, BINLookupError) as e:
    print(e)
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.