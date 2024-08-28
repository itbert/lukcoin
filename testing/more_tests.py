import unittest
from telegram import Update
from telegram.ext import CallbackContext
from my_telegram_bot import start_command, help_command, echo_command


class TestTelegramBot(unittest.TestCase):

    def setUp(self):
        self.update = Update(update_id=12345, message=None)
        self.context = CallbackContext(bot=None)

    def test_start_command(self):
        self.update.message = type('Message', (object,), {'text': '/COMMAND', 'chat': type('Chat', (object,), {'id': 123})})
        response = start_command(self.update, self.context)
        self.assertEqual(response, "Добро пожаловать в бота!")

    def test_help_command(self):
        self.update.message = type('Message', (object,), {'text': '/COMMAND', 'chat': type('Chat', (object,), {'id': 123})})
        response = help_command(self.update, self.context)
        self.assertEqual(response, "Список доступных команд: /start, /help")

    def test_echo_command(self):
        self.update.message = type('Message', (object,), {'text': 'Привет', 'chat': type('Chat', (object,), {'id': 123})})
        response = echo_command(self.update, self.context)
        self.assertEqual(response, "Привет")


if __name__ == '__main__':
    unittest.main()
