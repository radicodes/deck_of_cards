from random import shuffle

SUITS = ['hearts', 'spades', 'diamonds', 'clubs']
VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def print(self):
         print(f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.deck_stack = []
        for suit in SUITS:
            for value in VALUES:
                self.deck_stack.append(Card(value,suit))

    def shuffle(self):
        shuffle(self.deck_stack)


    def deal_one_card(self):
        if len(self.deck_stack) > 0:
            return self.deck_stack.pop()
        else:
            print("Deck is empty")

deck = Deck()
deck.shuffle()
for x in range(5):
    deck.deal_one_card().print()