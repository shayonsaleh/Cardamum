import unittest

from Card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("A", "S")
        self.card2 = Card.from_str("Kd")

    def test_rank(self):
        self.assertEqual(self.card1.get_rank(), "A")
        self.assertEqual(self.card2.get_rank(), "K")

    def test_suit(self):
        self.assertEqual(self.card1.get_suit(), "Spades")
        self.assertEqual(self.card2.get_suit(), "Diamonds")

    def test_str(self):
        self.assertEqual(str(self.card1), "As")
        self.assertEqual(str(self.card2), "Kd")


if __name__ == '__main__':
    unittest.main()
