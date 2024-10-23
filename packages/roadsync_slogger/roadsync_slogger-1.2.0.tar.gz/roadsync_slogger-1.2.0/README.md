
# `SLogger`

`SLogger` is a structured logger inspired by Go's `slog`, designed to simplify logging with key-value pairs in Python. It supports both plain text and JSON formats, with context fields being logged as top-level keys such as `username` and `request_id`.

## Installation

Install `SLogger` via pip:

```bash
pip install roadsync_slogger
```

## Basic Usage

`SLogger` logs messages along with additional context in a flat structure. Here's an example using the JSON format:

### JSON Logging Example
```python
from roadsync_slogger import SLogger

# Create SLogger instance with JSON format
logger = SLogger(format="json")

# Add initial context with username
logger = logger.with_fields(username="johndoe")

# Log a message with initial context
logger.info("User initialized session", request_id="abc123")
# Log output:
# {
#   "message": "User initialized session",
#   "username": "johndoe",
#   "request_id": "abc123"
# }
```

## Using `.with_fields()`

The `.with_fields()` method allows you to persist fields across multiple log calls. Each call to `.with_fields()` returns a new `SLogger` instance with the added fields, leaving the original context unchanged.

### Example:
```python
# Adding fields using .with_fields()
logger = logger.with_fields(username="johndoe", request_id="abc123")

# Logging with the updated context
logger.info("Performed a profile update", action="update_profile")
# Log output:
# {
#   "message": "Performed a profile update",
#   "username": "johndoe",
#   "request_id": "abc123",
#   "action": "update_profile"
# }
```

## Adding Context

You can continue adding fields with subsequent calls to `.with_fields()`, merging new context with existing fields. This allows for flexibility when extending the log context.

### Example with Added Context:
```python
# Initial logger with username field
logger = logger.with_fields(username="johndoe")

# Adding more context with action and request_id
logger = logger.with_fields(action="login", request_id="def456")
logger.info("Login successful")
# Log output:
# {
#   "message": "Login successful",
#   "username": "johndoe",
#   "request_id": "def456",
#   "action": "login"
# }
```

## Full Config
```python
@dataclass
class LogConfig:
    """
    Configuration for SLogger.

    Attributes:
        log_std: A callable for logging to stdout.
        log_err: A callable for logging to stderr.
        colors: A dictionary mapping log levels to their color codes.
        format: The log format, either "plain" or "json".
        json_formatter: A callable for formatting log entries in JSON.
        show_caller_info: A flag to include the caller's function name and line number.
    """
    log_std: Callable[[str], None]  # Function for logging to stdout (e.g., print)
    log_err: Callable[[str], None]  # Function for logging to stderr (e.g., print)
    colors: Dict[str, str]  # Colors for each log level
    format: str  # Log format: "plain" or "json"
    json_formatter: Callable[[Dict[str, Any]], bytes]  # Custom JSON formatter
    show_caller_info: bool  # Flag to include caller's function name and line number

full_config = LogConfig(...)

# Create SLogger instance with the full configuration
logger = SLogger(config=full_config)

```

## Override Defaults
```python
# Is the same as a new default config with just format and show_caller_info overriden
logger = SLogger(format='json', show_caller_info=True)
```
