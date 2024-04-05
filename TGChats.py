import logging
import time


class TGChats:
    @staticmethod
    def search_public_chat(tg, username: str):
        """
        Method to search public chat by username.

        Args:
            tg: Object of Telegram Class
            username: Username of user or Bot for search
        """

        logger = logging.getLogger("telegram_client")

        if username is None or len(username) <= 0:
            logger.info(f"Search public chat, username check failed - {username}")
            return False

        data = {
            "@type": "searchPublicChat",
            "username": f"@{username}"
        }

        public_chat = tg._send_data(data)
        public_chat.wait()

        if public_chat.error:
            logger.info(f"Failed search public chat: {public_chat.error_info}")
            return False
        else:
            logger.info(f'search_public_chat: {public_chat.update}')

            return public_chat.update

    @staticmethod
    def send_simple_message(tg, chat_id, text):
        """
        Method for sending message with passed text to passed chat.

        Args:
            tg: Object of Telegram Class
            chat_id: Chat ID of receiver
            text: Simple text for sending
        """
        logger = logging.getLogger("telegram_client")

        message = tg.send_message(
            chat_id=chat_id,
            text=text
        )
        message.wait()

        if message.error:
            logger.info(f"Failed send start message: {message.error_info}")
            return False
        else:
            logger.info(f'Start message sent: {message.update}')
            return message.update

    @staticmethod
    def get_message_history(tg, chat_id, limit=1):
        """
        Method for getting history from chat.

        Args:
            tg: Object of Telegram Class
            chat_id: Chat ID with history
            limit: Limit of messages which you want to receive, 1 by default
        """
        logger = logging.getLogger("telegram_client")

        data = {
            "@type": "getChatHistory",
            "chat_id": chat_id,
            "limit": limit
        }

        chat_history = tg._send_data(data)
        chat_history.wait()

        if chat_history.error:
            logger.info(f"Failed get message history: {chat_history.error_info}")
            return False
        else:
            logger.info(f'get_message_history: {chat_history.update}')

            return chat_history.update
