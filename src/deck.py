"""
Deck management module for card games.

This module provides the Deck class for creating, shuffling, and dealing
cards from a standard 52-card deck. It depends on the card module for
basic card components and the Card class.
"""

import random
from src.card import suits, ranks, values, Card

class Deck:
    """
    Represents a deck of playing cards with shuffle and deal functionality.
    
    The Deck class manages a collection of Card objects representing a standard
    52-card deck. It provides methods to shuffle the deck and deal individual
    cards. Cards are dealt from the top of the deck (end of the list).
    
    Attributes:
        all_cards (list): A list containing all Card objects in the deck
    """
    
    def __init__(self):
        """
        Initialize a new Deck with all 52 standard playing cards.
        
        Creates a complete deck by generating one Card object for each
        combination of suit and rank. The deck is created in a predictable
        order (not shuffled) and contains exactly 52 cards.
        """
        self.all_cards = []
        
        # Create one card for each combination of suit and rank
        for suit in suits:
            for rank in ranks:
                created_cards = Card(suit, rank)  # Create new Card instance
                self.all_cards.append(created_cards)  # Add to deck
                
    def shuffle(self):
        """
        Randomly shuffle all cards in the deck.
        
        Uses Python's random.shuffle() to randomize the order of cards
        in the deck. This modifies the deck in-place and does not return
        anything.
        """
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        """
        Deal and return one card from the top of the deck.
        
        Removes and returns the last card from the deck (representing the
        top of the deck). This reduces the deck size by one card.
        
        Returns:
            Card: The card that was dealt from the top of the deck
            
        Raises:
            IndexError: If attempting to deal from an empty deck
        """
        return self.all_cards.pop()  # Remove and return the top card