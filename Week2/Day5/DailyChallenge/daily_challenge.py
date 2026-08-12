# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP Concepts
# OOP Implementation (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation


# Key Python Topics:

# OOP (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation (random.shuffle())
# Instructions:

# Exercise 1: Quiz
# Answer the following questions:

# What is a class: A blueprint for creating objects.
# What is an instance: A specific object created from a class.
# What is encapsulation: Bundling data and the behavior that operates on that data inside a class, and controlling how that data can be accessed and modified from the outside.
# What is abstraction: Hiding how something works internally and only exposing what it does. This lets the user interact with a simple interface without the user needing to know the implementation details.
# What is inheritance: Where one class (child) automatically gets the attributed and methods of the parent class.
# What is multiple inheritance: Same as single inheritance, but where the child class has multiple parent classes.
# What is polymorphism: The ability for different classes to respond to the same method call in a different way.
# What is method resolution order or MRO: The order which Python searches through a class ancestors to find a method or attribute. More relevant with multiple inheritance, where parent classes have methods with the same name.

# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random


class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"'{self.value}' of {self.suit}"


class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        self.cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]
        print("Shuffling the deck...")
        random.shuffle(self.cards)

    def deal(self):
        dealt_card = self.cards.pop()
        print(f"Card dealt: {dealt_card}")
        return dealt_card

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Deck: {self.cards}\nNumber of cards: {len(self.cards)}"


deck = Deck()
print(deck)
deck.deal()
deck.deal()
deck.deal()
print(deck)
