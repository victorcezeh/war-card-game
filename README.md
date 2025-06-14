# War Card Game

A Python implementation of the classic card game "War" where two players compete by playing cards from their hands until one player collects all the cards.

## Game Rules

War is a simple card game played with a standard 52-card deck:

1. **Setup**: The deck is shuffled and split evenly between two players (26 cards each).
2. **Gameplay**: Players simultaneously play one card from the bottom of their hand.
3. **Winning Rounds**: The player with the higher card value wins both cards and adds them to their hand.
4. **War Scenario**: When both players play cards of equal value, a "war" occurs:
   - Each player plays 5 additional cards.
   - The player with the higher final card wins all cards from the battle.
   - If a player doesn't have enough cards for war, they lose immediately.
5. **Victory**: The game continues until one player runs out of cards.

## Card Values

Cards are ranked from lowest to highest:
- Two (2) through Ten (10): Face value
- Jack (11), Queen (12), King (13), Ace (14)

## Project Structure

```
war-card-game/
├── main.py              # Entry point script
├── src/
│   ├── card.py          # Card class and constants
│   ├── deck.py          # Deck class for card management
│   ├── player.py        # Player class for hand management
│   └── game.py          # Main game logic
└── README.md            # This file
```

## Installation

1. Clone or download the project files.
2. Ensure you have Python 3.6 or higher installed.
3. No additional dependencies are required (uses only Python standard library).

## Usage

Run the game from the project root directory:

```bash
python main.py
```

The game will automatically:
- Create two players ("One" and "Two").
- Shuffle and deal cards.
- Play rounds until someone wins.
- Display round numbers and war announcements.
- Announce the winner.

## Code Architecture

### Core Classes

**Card (`src/card.py`)**
- Represents a single playing card with suit, rank, and numerical value.
- Supports string representation for display.

**Deck (`src/deck.py`)**
- Manages a complete 52-card deck.
- Provides shuffling and card dealing functionality.
- Creates cards using all combinations of suits and ranks.

**Player (`src/player.py`)**
- Represents a game player with a hand of cards.
- Handles adding cards to hand and playing cards from hand.
- Plays cards from bottom of hand, receives cards at end of hand.

**Game Logic (`src/game.py`)**
- Contains the main game loop and war resolution logic.
- Manages round-by-round gameplay.
- Handles win conditions and war scenarios.

### Key Features

- **Automatic Game Management**: Handles all game state and rule enforcement.
- **War Resolution**: Properly implements the war mechanic when cards tie.
- **Win Condition Checking**: Detects when players run out of cards.
- **Round Tracking**: Displays current round number.
- **Edge Case Handling**: Manages scenarios where players can't participate in war.

## Example Output

```
Round: 1.
Round: 2.
WAR!
Round: 3.
...
Player two has no more cards! Player one wins the game.
```

## Technical Details

- **Card Dealing**: Cards are dealt alternately to ensure even distribution.
- **War Mechanic**: Requires 5 cards minimum to participate in war.
- **Memory Management**: Uses list operations (pop/append/extend) for card movement.
- **Game State**: Tracks round numbers and player card counts.
- **Random Shuffling**: Uses Python's `random.shuffle()` for fair card distribution.

## Customization

The game can be easily modified:
- Change player names in `game.py`
- Adjust card values in `card.py`
- Modify war requirements (currently 5 cards).
- Add additional players (requires game logic changes).

## Educational Value

This implementation demonstrates:
- Object-oriented programming principles.
- Game state management.
- List manipulation and data structures.
- Control flow and loop logic.
- Module organization and imports.
- Python best practices and documentation.

## Author

I created this as a Python learning project.