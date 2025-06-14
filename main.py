"""
War Card Game Entry Point

This is the main entry point script for the War card game application.
It imports and executes the main game function when the script is run directly.

Usage:
    python main.py

The script uses the standard Python idiom to ensure the game only runs
when this file is executed directly, not when imported as a module.
"""

from src.game import main

# Execute the game only when this script is run directly
# This prevents the game from starting if this file is imported elsewhere
if __name__ == "__main__":
    main()  # Start the War card game