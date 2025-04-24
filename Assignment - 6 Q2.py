import random
class RockPaperScissors:
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        else:
            return "computer"
    
    def play_round(self, user_choice):
        if user_choice not in self.choices:
            print("Invalid choice. Please select rock, paper, or scissors.")
            return
        
        computer_choice = self.get_computer_choice()
        print(f"Round {self.current_round}:")
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        winner = self.find_winner(user_choice, computer_choice)
        if winner == "user":
            self.user_wins += 1
            print("You win this round!")
        elif winner == "computer":
            self.computer_wins += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")
        
        self.current_round += 1
    
    def check_game_winner(self):
        if self.current_round > self.total_rounds:
            print("\nGame Over!")
            if self.user_wins > self.computer_wins:
                print(f"You win the game! Final score - You: {self.user_wins}, Computer: {self.computer_wins}")
            elif self.computer_wins > self.user_wins:
                print(f"Computer wins the game! Final score - You: {self.user_wins}, Computer: {self.computer_wins}")
            else:
                print(f"The game is a draw! Final score - You: {self.user_wins}, Computer: {self.computer_wins}")
            return True
        return False

    def play_game(self):
        while self.current_round <= self.total_rounds:
            print(f"\nRound {self.current_round} of {self.total_rounds}")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            self.play_round(user_choice)
            if self.check_game_winner():
                break

rounds = int(input("Enter number of rounds to play: "))
game = RockPaperScissors(rounds)
game.play_game()
