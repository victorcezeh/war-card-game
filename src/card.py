"""
Card game module providing basic card representation.

This module defines the fundamental components for a standard 52-card deck,
including card suits, ranks, and values for card game implementations.
"""

# Standard playing card suits in a typical deck
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Card ranks from lowest to highest (Two through Ace)
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Numerical values assigned to each rank for comparison purposes
# Ace is high (value 14) in this implementation
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    """
    Represents a single playing card with suit, rank, and numerical value.
    
    A Card object encapsulates the three key properties of a playing card:
    - suit: The card's suit (Hearts, Diamonds, Spades, or Clubs)
    - rank: The card's rank (Two through Ace)
    - value: The numerical value associated with the rank for comparisons
    
    Attributes:
        suit (str): The suit of the card
        rank (str): The rank of the card
        value (int): The numerical value of the card based on its rank
    """
    
    def __init__(self, suit, rank):
        """
        Initialize a new Card instance.
        
        Args:
            suit (str): The suit of the card (must be one of the valid suits)
            rank (str): The rank of the card (must be one of the valid ranks)
        
        The card's numerical value is automatically assigned based on the rank
        using the global values dictionary.
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # Look up numerical value from global values dict
        
    def __str__(self):
        """
        Return a string representation of the card.
        
        Returns:
            str: A formatted string showing the card's rank and suit
                 (e.g., "Ace of Spades.")
        """
        return f"{self.rank} of {self.suit}."