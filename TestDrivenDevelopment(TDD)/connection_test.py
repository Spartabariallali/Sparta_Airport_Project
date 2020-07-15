import unittest
import pytest
from create_connection import Database_OOP

class Connection_Test(unittest.TestCase):
    object = Database_OOP()

    def test_connection(self):
        self.assertEqual(self.object.establish_connection(), connection.cursor())