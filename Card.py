class Card:
    """Playing card class"""

    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

    def __init__(self, rank, suit):
        # Store rank and suit as integers to allow for different output representations
        self.rank = self.convert_to_rank(rank)
        self.suit = self.convert_to_suit(suit)

    def get_suit(self):
        return self.suits[self.suit]

    def get_rank(self):
        return self.ranks[self.rank - 1]

    def __str__(self):
        return self.get_rank() + self.get_suit()[0].lower()

    def convert_to_suit(self, input_suit):
        """
        Generic function that converts many inputs to best possible guess of suit

        :param input_suit: Any
        :return: Integer where 0 == Spades, 1 == Hearts, 2 == Diamonds, 3 == Clubs
        """
        try:
            int_val = int(input_suit)
        except ValueError:
            # Not a int, check if non-empty string and convert to int
            if isinstance(input_suit, str) and len(input_suit) > 0:
                for i, suit in enumerate(self.suits):
                    if suit.upper() == input_suit.upper() or suit[0].upper() == input_suit[0].upper():
                        int_val = i
                        break
        if 0 <= int_val <= 3:
            return int_val
        else:
            raise ValueError("Integer outside of acceptable range for suit (0 - 3)")

    def convert_to_rank(self, input_rank):
        """
        Generic function that converts many inputs to best possible guess of rank

        :param input_rank: Any
        :return: Integer between 1 and 13
        """
        try:
            int_val = int(input_rank)
        except ValueError:
            # Not a int, check if non-empty string and convert to int
            if isinstance(input_rank, str) and len(input_rank) > 0:
                for i, rank in enumerate(self.ranks):
                    if rank.upper() == input_rank.upper() or rank[0].upper() == input_rank[0].upper():
                        int_val = i + 1
                        break
        if 1 <= int_val <= 13:
            return int_val
        else:
            raise ValueError("Integer outside of acceptable range for rank (1 - 13)")

    @classmethod
    def from_str(cls, input_str):
        if len(input_str) == 2:
            return cls(input_str[0], input_str[1])