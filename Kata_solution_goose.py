import random

class GooseGame:
    def __init__(self):
        self.players = []
        self.positions = {}
        self.the_goose = [5, 9, 14, 18, 23, 27]

    def add_player(self, name):
        if name in self.players:
            print(f"{name}: already existing player")
        else:
            self.players.append(name)
            self.positions[name] = "Start"
            print(f"players: {', '.join(self.players)}")

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def move_player(self, name, roll1=None, roll2=None):
        if roll1 is None and roll2 is None:
            roll1, roll2 = self.roll_dice()
    
        def handle_goose(start_position, move_to, roll_sum):
            while move_to in self.the_goose:
                print(f"{name} moves from {start_position} to {move_to}, The Goose. {name} moves again and goes to {move_to + roll_sum}")
                start_position, move_to = move_to, move_to + roll_sum
            return move_to
    
        start_position = 0 if self.positions[name] == "Start" else self.positions[name]
        move_sum = roll1 + roll2
        move_to = start_position + move_sum
    
        # Handle landing on The Bridge at position 6
        if move_to == 6:
            print(f"{name} rolls {roll1},{roll2}. {name} moves from {start_position} to The Bridge. {name} jumps to 12")
            move_to = 12
        else:
            # Initial move announcement
            print(f"{name} rolls {roll1},{roll2}. {name} moves from {start_position} to {move_to}")
    
        # Adjust for overshooting or exact landing on 63
        if move_to > 63:
            overshoot = move_to - 63
            move_to = 63 - overshoot  # Calculate the bounce-back position
            print(f"{name} bounces! {name} returns to {move_to}")
        elif move_to == 63:
            print(f"{name} Wins!!")
            self.positions[name] = move_to
            return True
    
        move_to = handle_goose(start_position, move_to, move_sum)
    
        # Handle the prank if the position is occupied by another player
        for other_player, other_position in self.positions.items():
            if other_player != name and other_position == move_to:
                self.positions[other_player] = start_position
                print(f"On {move_to} there is {other_player}, who returns to {start_position}")
    
        self.positions[name] = move_to
    
        # Final victory check after all moves, including pranks and goose jumps
        if move_to >= 63:
            if move_to == 63:
                print(f"{name} Wins!!")
                return True
            else:  # Handle potential overshoot adjustments not covered earlier
                overshoot = move_to - 63
                move_to = 63 - overshoot
                print(f"{name} bounces! {name} returns to {move_to}")
                self.positions[name] = move_to
    
        return False




    def start_game(self):
        print("Starting the game with players:", ", ".join(self.players))
        while True:
            for player in self.players:
                dice_input = input(f"{player} rolls: ").strip()
                if dice_input:  # If the player inputs something
                    try:
                        roll1, roll2 = map(int, dice_input.split(","))
                        if self.move_player(player, roll1, roll2):
                            return  # End the game if a player wins.
                    except ValueError:
                        print("Invalid input. Please enter the rolls in the format 'x,y'.")
                else:  # If the player inputs nothing, automatically roll the dice.
                    if self.move_player(player):
                        return

    def add_players_loop(self):
        while True:
            player_name = input("Add player: ").strip()
            if player_name == "":
                break
            self.add_player(player_name)

        if len(self.players) > 0:
            self.start_game()
        else:
            print("No players added. Exiting.")

def main():
    game = GooseGame()
    game.add_players_loop()

if __name__ == "__main__":
    main()
