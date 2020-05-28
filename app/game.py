from app import app
from flask import Flask
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        self.usedcards = []
        self.build()
        self.shuffle()

    def build(self):
        print ("build card deck")
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        card1 = self.cards.pop()

        i = 0
        if len(self.cards)>0:
            for card3 in self.cards:
                i += 1
                print ("i="+str(i) + str(card3.suit) + str(card3.value))

        return card1
