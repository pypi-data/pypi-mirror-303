from enum import Enum
import orjson
from typing import Callable, Dict, Any, Optional, Union
from datetime import datetime, timezone
from dataclasses import asdict, dataclass, is_dataclass, replace
import inspect
import traceback
import sys
from decimal import Decimal

# Define log levels using Enum for clarity and safety
class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

# Helper function to convert string log level to LogLevel enum
def get_log_level(level: Union[str, LogLevel]) -> LogLevel:
    if isinstance(level, LogLevel):
        return level
    level = level.upper()
    if level == "DEBUG":
        return LogLevel.DEBUG
    elif level == "INFO":
        return LogLevel.INFO
    elif level == "WARNING":
        return LogLevel.WARNING
    elif level == "ERROR":
        return LogLevel.ERROR
    elif level == "CRITICAL":
        return LogLevel.CRITICAL
    else:
        raise ValueError(f"Invalid log level: {level}")

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
        log_level: The minimum log level to write out.
    """
    log_std: Callable[[str], None]                      # Function for logging to stdout (e.g., print)
    log_err: Callable[[str], None]                      # Function for logging to stderr (e.g., print)
    colors: Dict[str, str]                              # Colors for each log level
    format: str                                         # Log format: "plain" or "json"
    json_formatter: Callable[[Dict[str, Any]], bytes]   # Custom JSON formatter
    show_caller_info: bool                              # Flag to include caller's function name and line number
    log_level: Union[str, LogLevel]                     # Log level

# Default config with previous values
def default_config(**kwargs) -> LogConfig:
    # Default configuration
    default_config = LogConfig(
        log_std=print,
        log_err=lambda x: print(x, file=sys.stderr),
        colors={
            "DEBUG": "\033[94m",        # Blue
            "INFO": "\033[92m",         # Green
            "WARNING": "\033[93m",      # Yellow
            "ERROR": "\033[91m",        # Red
            "CRITICAL": "\033[95m",     # Magenta
            "reset": "\033[0m"          # Reset color
        },
        format="plain",                 # Default format
        json_formatter=orjson.dumps,    # Default JSON formatter
        show_caller_info=False,         # By default, do not show caller info
        log_level=LogLevel.DEBUG,       # Minimum log level
    )
    
    # Update the fields with values from kwargs
    return replace(default_config, **kwargs)

class SLogger:
    """
    A structured logger that supports plain text and JSON formats.

    Methods:
        with_fields: Returns a new SLogger instance with additional context fields.
        log: Logs a message with the given level and context.
        debug: Logs a debug message.
        info: Logs an info message.
        warning: Logs a warning message.
        error: Logs an error message.
        critical: Logs a critical message.
        exception: Logs an error message with exception info.
    """
    def __init__(self, config: Optional[LogConfig] = None, **kwargs):
        """
        Initialize the logger with the provided configuration.

        Args:
            config: The LogConfig object containing logger settings.
            **kwargs: Fields to override in the default configuration.
        """
        # If no config is provided, generate a default one, and allow overrides via kwargs
        if config is None:
            config = default_config(**kwargs)
        else:
            # If config is provided, use replace to override specific fields using kwargs
            config = replace(config, **kwargs)

        config.log_level = get_log_level(config.log_level)

        self.context = {}
        self.config = config

    def with_fields(self, fields: Optional[Any] = None, **kwargs) -> 'SLogger':
        """
        Return a new SLogger instance with additional fields added to the context.

        Args:
            fields: A dictionary, dataclass, or any object to add to the logger's context.
            **kwargs: Additional key-value pairs to add to the logger's context.

        Returns:
            A new SLogger instance with updated context.
        """
        # Initialize an empty dictionary for combined fields
        combined_fields: Dict[str, Any] = {}

        # Check if fields is a dataclass and convert to dictionary if true
        if is_dataclass(fields):
            combined_fields.update(asdict(fields))  # type: ignore # Convert dataclass to dict

        # If fields is a dictionary, update the combined_fields and check for dataclass values
        elif isinstance(fields, dict):
            combined_fields.update({k: _convert_dataclass(v) for k, v in fields.items()})

        # For any other type, cast to string and use the type as the key
        elif fields is not None:
            combined_fields[type(fields).__name__] = str(fields)

        # Process kwargs: Convert any kwarg value that is a dataclass into a dictionary
        kwargs = {k: _convert_dataclass(v) for k, v in kwargs.items()}

        # Add the kwargs to the combined fields (kwargs take precedence)
        combined_fields.update(kwargs)

        context = {
            f"_{k}" if k in {"message", "level", "timestamp"} else k: v
            for k, v in {**self.context, **combined_fields}.items()
        }

        # Merge the existing context with the new combined fields
        new_logger = SLogger(self.config)
        new_logger.context = context
        return new_logger

    def log(self, level: LogLevel, msg: str, **extra_fields):
        """
        Log a message at the specified level with additional context.

        Args:
            level: The log level (e.g., "DEBUG", "INFO", "ERROR").
            msg: The log message.
            **extra_fields: Additional key-value pairs to include in the log entry.
        """
        
        if level.value < self.config.log_level.value: # type: ignore
            return  # Don't log messages below the current log level

        # Convert any dataclass in extra_fields into a dictionary
        extra_fields = {k: _convert_dataclass(v) for k, v in extra_fields.items()}

        # Combine with context
        current_time = datetime.now(timezone.utc)
        log_context = {**self.context, **extra_fields}

        # Optionally include caller information
        if self.config.show_caller_info:
            frame = inspect.stack()[2]
            caller_info = f"{frame.function}:{frame.lineno}"
            log_context['caller'] = caller_info

        # Format the message according to the selected format (json or plain)
        if self.config.format == "json":
            log_message = self._format_as_json(level.name, current_time, msg, log_context)
            self.config.log_std(log_message) if level != LogLevel.ERROR else self.config.log_err(log_message)
        else:
            log_message = self._format_as_plain(level.name, current_time, msg, log_context)
            self.config.log_std(log_message) if level != LogLevel.ERROR else self.config.log_err(log_message)

    def _format_as_json(self, level: str, time: datetime, msg: str, context: Dict[str, Any]) -> str:
        """
        Format a log entry as a JSON string.

        Args:
            level: The log level (e.g., "DEBUG", "INFO", "ERROR").
            time: The current timestamp as a datetime object.
            msg: The log message.
            context: The context fields to include in the log entry.

        Returns:
            A JSON-formatted string.
        """
        log_entry = {"level": level, "timestamp": time.isoformat(), "message": msg}
        if context:
            log_entry.update(context)
        # Process log_entry to serialize unknown types
        log_entry = serialize_value(log_entry)
        return self.config.json_formatter(log_entry).decode("utf-8")

    def _format_as_plain(self, level: str, time: datetime, msg: str, context: Dict[str, Any]) -> str:
        """
        Format a log entry as a plain text string.

        Args:
            level: The log level (e.g., "DEBUG", "INFO", "ERROR").
            time: The current time as a datetime object (short format).
            msg: The log message.
            context: The context fields to include in the log entry.

        Returns:
            A plain text formatted string.
        """
        short_time = time.astimezone().strftime('%-I:%M%p').upper()
        color = self.config.colors.get(level, "")
        context_str = ', '.join([f"{key}={value}" for key, value in context.items()])
        log_message = f"{color}[{level}]{self.config.colors['reset']} [{short_time}] {msg}{', ' + context_str if context_str else ''}"
        return log_message

    def debug(self, msg: str, **extra_fields):
        """
        Log a debug message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.DEBUG, msg, **extra_fields)

    def info(self, msg: str, **extra_fields):
        """
        Log an info message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.INFO, msg, **extra_fields)

    def warning(self, msg: str, **extra_fields):
        """
        Log a warning message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.WARNING, msg, **extra_fields)

    def warn(self, msg: str, **extra_fields):
        """
        Log a warning message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.WARNING, msg, **extra_fields)

    def error(self, msg: str, **extra_fields):
        """
        Log an error message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.ERROR, msg, **extra_fields)

    def critical(self, msg: str, **extra_fields):
        """
        Log a critical message.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        self.log(LogLevel.CRITICAL, msg, **extra_fields)

    def exception(self, msg: str, **extra_fields):
        """
        Log an error message along with exception information.

        Args:
            msg: The log message.
            **extra_fields: Additional context to include in the log entry.
        """
        exc_type, exc_value, exc_traceback = sys.exc_info()

        # Formatting the traceback similar to logging.exception output
        error = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        extra_fields['error'] = error

        self.log(LogLevel.ERROR, msg, **extra_fields)

    def __repr__(self) -> str:
        return f"<SLogger context={self.context}>"

def _convert_dataclass(value: Any) -> Any:
    """
    Helper function to convert dataclass instances or objects with a `to_dict` method to dictionaries.
    If neither applies, the value is returned unchanged.
    """
    # Check if the value has a `to_dict` method and call it if available
    if hasattr(value, "to_dict") and callable(getattr(value, "to_dict")):
        return value.to_dict()

    # Check if the value is a dataclass and convert it to a dictionary
    if is_dataclass(value):
        return asdict(value)  # type: ignore

    # If the value has a __dict__, return the __dict__
    if hasattr(value, '__dict__'):
        return value.__dict__

    # Return the value as-is if no conversion is needed
    return value

def serialize_value(value: Any) -> Any:
    """
    Recursively serialize values to make them JSON serializable.

    Args:
        value: The value to serialize.

    Returns:
        A JSON-serializable representation of the value.
    """
    if isinstance(value, dict):
        return {k: serialize_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [serialize_value(v) for v in value]
    elif isinstance(value, tuple) and hasattr(value, '_fields'):
        return {field: serialize_value(getattr(value, field)) for field in value._fields}
    elif isinstance(value, tuple):
        return [serialize_value(v) for v in value]
    elif isinstance(value, (set, frozenset)):
        return [serialize_value(v) for v in value]
    elif isinstance(value, Decimal):
        return str(value)
    elif isinstance(value, (int, float, str, bool, type(None))):
        return value
    elif isinstance(value, datetime):
        return value.isoformat()
    elif hasattr(value, '__dict__'):
        return serialize_value(value.__dict__)
    else:
        return str(value)  # Fallback to string representation
