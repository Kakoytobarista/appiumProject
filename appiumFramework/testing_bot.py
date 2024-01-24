import os
from dotenv import load_dotenv

import testingbotclient

load_dotenv()


class TestingBotStatus:
    def __init__(self):
        self.testing_bot = testingbotclient.TestingBotClient(os.getenv('KEY'), os.getenv('SECRET'))

    def set_status(self, session_id):
        self.testing_bot.tests.update_test(session_id, passed=1 | 0)
