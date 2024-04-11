## Game Mechanics and Key Functions

### `__init__(self)`
- Initializes a new game instance, setting up the players list and their positions on the board.

### `add_player(self, name)`
- Adds a new player to the game, ensuring no duplicate names are allowed. It updates the game state with the new player and their starting position.

### `roll_dice(self)`
- Simulates rolling two six-sided dice, returning a tuple with the outcomes. This function is used for automatic dice rolls when players opt not to input their rolls manually.

### `move_player(self, name, roll1=None, roll2=None)`
- Moves a player based on the roll of the dice. This function handles the complexities of game movement, including:
    - Automatic and manual dice rolls.
    - Special spaces like "The Bridge" and "The Goose," which modify player movement.
    - The "Prank" mechanism, where landing on an occupied space causes players to swap positions.
    - Victory conditions and handling overshooting space 63.
    - The function also manages bouncing back from space 63 if a player overshoots it.

### `start_game(self)`
- Begins the game loop, prompting each player to roll the dice (either automatically or by entering a roll manually) and managing the turn sequence. It continues until a player wins by landing exactly on space 63.

### `add_players_loop(self)`
- Manages the initial phase of the game where players are added. This loop runs until the user indicates that no more players will be added, at which point the game starts.

### `main()`
- The entry point for the game. It creates a new game instance and starts the player addition loop.

## How to Play

1. Run the script with `Kata_solution_goose.py`.
2. Follow the on-screen instructions to add players and start the game.


