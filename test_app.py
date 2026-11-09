import unittest
from app import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_uses_name(self):
        self.assertEqual(greeting("Denny"), "Hello, Denny!")


if __name__ == "__main__":
    unittest.main()
