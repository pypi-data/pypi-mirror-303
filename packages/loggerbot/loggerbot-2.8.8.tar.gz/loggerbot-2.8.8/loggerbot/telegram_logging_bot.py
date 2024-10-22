# © N.Sikharulidze (https://ubix.pro/)
import requests
import os
import sys
import logging
from typing import Union, List
import time
from queue import Queue
import threading

class TelegramLoggingBot:
    def __init__(self, tg_token: str, chat_ids: Union[str, List[str]], log_level=logging.INFO, rate_limit=20, time_window=60):
        self.tg_token = tg_token
        self.chat_ids = [chat_ids] if isinstance(chat_ids, str) else chat_ids
        if not self.tg_token or not self.chat_ids:
            raise ValueError("tg_token and chat_ids must be provided")
        self.base_url = f"https://api.telegram.org/bot{self.tg_token}/sendMessage"
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.message_queue = Queue()
        self.rate_limit = rate_limit
        self.time_window = time_window
        self.last_sent = []
        self.queue_processor = threading.Thread(target=self._process_queue, daemon=True)
        self.queue_processor.start()

    def _send_message(self, log_status, user_text):
        file_name = os.path.basename(sys.argv[0])
        message = (
            f"<b>{log_status} from {file_name}</b>\n"
            f"{user_text}"
        )
        self.message_queue.put((message, time.time()))

    def _process_queue(self):
        while True:
            message, timestamp = self.message_queue.get()
            self._send_rate_limited(message)
            self.message_queue.task_done()

    def _send_rate_limited(self, message):
        current_time = time.time()
        self.last_sent = [t for t in self.last_sent if current_time - t < self.time_window]
        
        if len(self.last_sent) >= self.rate_limit:
            sleep_time = self.time_window - (current_time - self.last_sent[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        params = {
            "text": message,
            "parse_mode": "html"
        }
        
        results = []
        for chat_id in self.chat_ids:
            params["chat_id"] = chat_id
            full_url = self.base_url
            self.logger.debug(f"Sending message to URL: {full_url}")
            self.logger.debug(f"Request parameters: {params}")
            try:
                response = requests.get(full_url, params=params)
                self.logger.debug(f"Response status code: {response.status_code}")
                self.logger.debug(f"Response content: {response.text}")
                response.raise_for_status()
                result = response.json()
                if result.get('ok'):
                    self.logger.info(f"Message sent successfully to chat {chat_id}")
                else:
                    self.logger.error(f"Failed to send message to chat {chat_id}. Error: {result.get('description')}")
                results.append(result)
                self.last_sent.append(time.time())
            except requests.RequestException as e:
                self.logger.error(f"Error sending message to Telegram chat {chat_id}: {e}")
                results.append(None)
        return results

    def debug(self, text):
        self.logger.debug(text)
        return self._send_message("🐛 DEBUG", text)

    def info(self, text):
        self.logger.info(text)
        return self._send_message("ℹ️ INFO", text)

    def warning(self, text):
        self.logger.warning(text)
        return self._send_message("⚠️ WARNING", text)

    def error(self, text):
        self.logger.error(text)
        return self._send_message("❌ ERROR", text)

    def critical(self, text):
        self.logger.critical(text)
        return self._send_message("🚨 CRITICAL", text)

    def alert(self, text):
        self.logger.warning(text)  # Using warning level for alert
        return self._send_message("🚨 ALERT", text)

    def complete(self, text):
        self.logger.info(text)  # Using info level for complete
        return self._send_message("✅ COMPLETE", text)

    def set_log_level(self, level):
        self.logger.setLevel(level)

# Alias for backward compatibility
LogBot = TelegramLoggingBot
