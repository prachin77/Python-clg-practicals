import random

class Card:
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, rank=None, suit=None):
        if rank is None and suit is None:
            self.randomCard()
        else:
            self.rank = rank
            self.suit = suit

    def randomCard(self):
        self.rank = random.choice(self.ranks)
        self.suit = random.choice(self.suits)

    def compareCard(self, anotherCard) -> bool:
        if self.rank == anotherCard.rank and self.suit == anotherCard.suit:
            return True
        else:
            return False

if __name__ == "__main__":
    card = Card()
    print(" ~~ Card Guesser ~~")
    while True:
        print("Guess the Card\n")
        rank = input("> Enter the Rank of your Card [Ace..6..10..Jack..King]: ")
        suit = input("> Enter the Suit of your Card [Clubs, Diamonds, Hearts, Spades]: ")
        guess = Card(rank, suit)

        if card.compareCard(guess):
            print("> Correct <")
            break
        else:
            print("!! Incorrect Guess !!")
