"""
Player management module for card games.

This module provides the Player class for representing individual players
in card games. Each player can hold cards, play cards, and receive new cards
during gameplay.
"""


class Player:
    """
    Represents a player in a card game with a hand of cards.
    
    The Player class manages an individual player's hand of cards, allowing
    them to play cards (remove from hand), receive cards (add to hand), and
    track their current card count. Players play cards from the bottom of
    their hand and receive cards at the end of their hand.
    
    Attributes:
        name (str): The player's name
        all_cards (list): A list containing all Card objects in the player's hand
    """
    
    def __init__(self, name):
        """
        Initialize a new Player with the given name and empty hand.
        
        Args:
            name (str): The name of the player
        
        The player starts with an empty hand (no cards).
        """
        self.name = name
        self.all_cards = []  # Start with empty hand
        
    def remove_one(self):
        """
        Play one card from the bottom of the player's hand.
        
        Removes and returns the first card from the player's hand
        (index 0, representing the bottom of the hand). This reduces
        the player's hand size by one card.
        
        Returns:
            Card: The card that was played from the bottom of the hand
            
        Raises:
            IndexError: If attempting to play a card when hand is empty
        """
        return self.all_cards.pop(0)  # Remove and return bottom card
    
    def add_cards(self, card):
        """
        Add one or more cards to the player's hand.
        
        Accepts either a single Card object or a list of Card objects
        and adds them to the end of the player's hand. This method
        handles both individual card additions and bulk card additions.
        
        Args:
            card (Card or list): Either a single Card object or a list
                                of Card objects to add to the hand
        """
        if type(card) == type([]):  # Check if card is a list
            self.all_cards.extend(card)  # Add all cards from list
        else:
            self.all_cards.append(card)  # Add single card
    
    def __str__(self):
        """
        Return a string representation of the player and their hand size.
        
        Returns:
            str: A formatted string showing the player's name and number
                 of cards in their hand (e.g., "Player, Alice has 5 card.")
        """
        return f"Player, {self.name} has {len(self.all_cards)} card."