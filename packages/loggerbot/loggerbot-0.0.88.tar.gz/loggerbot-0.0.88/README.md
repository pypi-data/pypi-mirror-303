# LoggerBot

© N.Sikharulidze (https://ubix.pro/)

LoggerBot is a Telegram logging library that allows you to send log messages to one or multiple Telegram chats using a bot. It provides an easy-to-use interface for logging various types of messages and includes features like rate limiting and message queuing.

## Features

- Send log messages to one or multiple Telegram chats
- Support for different log levels: debug, info, warning, error, critical, alert, and complete
- Rate limiting to prevent excessive API calls
- Message queuing for smooth operation
- Easy integration with existing Python logging
- Backward compatibility with the `LogBot` alias
- HTML formatting support for log messages

## Installation

You can install LoggerBot using pip:

```
pip install loggerbot
```

## Usage

Here's a basic example of how to use LoggerBot:

```python
from loggerbot import TelegramLoggingBot

# Initialize the bot with your Telegram bot token and chat ID(s)
log_bot = TelegramLoggingBot("YOUR_BOT_TOKEN", ["CHAT_ID_1", "CHAT_ID_2"])

# Send log messages
log_bot.info("This is an informational message")
log_bot.warning("This is a warning message")
log_bot.error("An error occurred")
log_bot.alert("This is an important alert")
log_bot.complete("Task completed successfully")
```

## Advanced Usage

### Rate Limiting

LoggerBot includes built-in rate limiting to prevent excessive API calls. You can customize the rate limit when initializing the bot:

```python
log_bot = TelegramLoggingBot("YOUR_BOT_TOKEN", "CHAT_ID", rate_limit=20, time_window=60)
```

This sets a limit of 20 messages per 60 seconds.

### Setting Log Level

You can set the minimum log level for the bot:

```python
import logging
log_bot.set_log_level(logging.DEBUG)
```

### Using with Python's logging module

LoggerBot can be integrated with Python's built-in logging module:

```python
import logging
from loggerbot import TelegramLoggingBot

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a TelegramLoggingBot instance
tg_handler = TelegramLoggingBot("YOUR_BOT_TOKEN", "CHAT_ID")

# Add the TelegramLoggingBot as a handler to the logger
logger.addHandler(tg_handler)

# Now you can use the logger as usual
logger.info("This message will be sent to Telegram")
```

### HTML Formatting for Log Messages

LoggerBot supports HTML formatting in log messages, allowing you to enhance the readability and structure of your logs in Telegram. Here are some examples of how to use HTML formatting:

```python
# Bold text
log_bot.info("This is an <b>important</b> message")

# Italic text
log_bot.warning("Please <i>be cautious</i> when proceeding")

# Code formatting
log_bot.error("An error occurred: <code>ValueError: Invalid input</code>")

# Underlined text
log_bot.alert("This requires <u>immediate attention</u>")

# Combining multiple formats
log_bot.complete("Task <b><i>successfully</i></b> completed")

# Using line breaks
log_bot.info("This is a multi-line message.<br>It has two lines.")

# Creating a list
log_bot.info("Steps to reproduce:<br>1. Open the app<br>2. Click on settings<br>3. Select 'Advanced'")

# Adding a hyperlink
log_bot.info("For more information, visit our <a href='https://example.com'>documentation</a>")
```

Note: Make sure to use HTML entities for special characters like `<` (`&lt;`), `>` (`&gt;`), and `&` (`&amp;`) when they're not part of HTML tags.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
