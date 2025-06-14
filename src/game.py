"""
War Card Game Implementation

This module implements the classic card game "War" where two players compete
by playing cards from their hands. The player with the higher card value wins
both cards. When cards have equal value, a "war" occurs where additional cards
are played to determine the winner.

Game Rules:
- Each player starts with 26 cards from a shuffled deck
- Players simultaneously play one card from their hand
- Higher card value wins both cards
- If cards are equal, players enter "war" by playing 5 additional cards
- Game continues until one player runs out of cards
"""

from src.card import Card
from src.deck import Deck
from src.player import Player

def main():
    """
    Main function to run the War card game.
    
    Sets up the game by creating two players, dealing cards from a shuffled deck,
    and running the main game loop until one player wins by collecting all cards
    or the other player cannot continue playing.
    
    Game Flow:
    1. Initialize players and deck
    2. Shuffle and deal 26 cards to each player
    3. Play rounds until someone wins
    4. Handle regular rounds and war scenarios
    """
    
# GAME SETUP
    # Create two players for the game
    player_one = Player("One")
    player_two = Player("Two")

    # Create and shuffle a new deck of cards
    new_deck = Deck()
    new_deck.shuffle()

    # Deal 26 cards to each player alternately
    for i in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    
    game_on = True  # Flag to control main game loop

    round_num = 0  # Track the current round number

    # MAIN GAME LOOP
    while game_on:
    
        round_num +=1
        print(f"Round: {round_num}.")
    
        # Check if player one is out of cards
        if len(player_one.all_cards) == 0:
            print("Player one has no more cards! Player two wins the game.")
            game_on = False
            break
    
        # Check if player two is out of cards
        if len(player_two.all_cards) == 0:
            print("Player two has no more cards! Player one wins the game.")
            game_on = False
            break
    
        # START A NEW ROUND
        # Each player plays one card to start the round
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
    
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
    
        # WAR RESOLUTION LOOP
        # Continue until someone wins the current battle
        at_war = True
    
        while at_war:
        
            # Player one wins this battle
            if player_one_cards[-1].value > player_two_cards[-1].value:
            
                # Player one takes all cards from this battle
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
            
                at_war = False
        
            # Player two wins this battle
            elif player_one_cards[-1].value < player_two_cards[-1].value:
            
                # Player two takes all cards from this battle
                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)
            
                at_war = False
            
            # Cards are equal - WAR scenario
            else:
                print("WAR!")
            
                # Check if player one has enough cards for war (needs 5 cards)
                if len(player_one.all_cards) < 5:
                    print("Player one unable to declare war!")
                    print("Player two wins!")
                    game_on = False
                    break
                # Check if player two has enough cards for war (needs 5 cards)
                elif len(player_two.all_cards) < 5:
                    print("Player two unable to declare war!")
                    print("Player one wins!")
                    game_on = False
                    break
                # Both players have enough cards - proceed with war
                else:
                    # Each player adds 5 more cards to the battle
                    for number in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())