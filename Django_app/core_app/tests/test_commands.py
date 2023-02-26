"""
Mocking test for Django management command
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.test import SimpleTestCase, TestCase
from django.db.utils import OperationalError
from django.core.management import call_command


# This Test class came from DRF lecture
@patch('core_app.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    @staticmethod
    def test_wait_for_db_ready(self, patched_check):
        print('\nDB Test 1: wait_for_db_ready')

        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        print('DB Test 2: wait_for_db_delay')

        patched_check.side_effect = [Psycopg2OpError] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        # patched_check should be called 6 times
        self.assertEqual(patched_check.call_count, 6)
        # patched_check should be called with databases=['default']
        patched_check.assert_called_with(databases=['default'])


# This Test code came from the ChatGPT
class WaitDBTest(TestCase):
    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, sleep_mock):
        with patch('core_app.management.commands.wait_for_db.Command.check') as check_mock:
            check_mock.return_value = True
            call_command('wait_for_db')

            self.assertEqual(check_mock.call_count, 1)
