import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
Win = 1
Draw = -1
Running = 0
Game = Running
select = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |")

def logika():
    global Game
    if (board[1] == board[2] == board[3] and board[1] != ' ') or \
       (board[4] == board[5] == board[6] and board[4] != ' ') or \
       (board[7] == board[8] == board[9] and board[7] != ' ') or \
       (board[1] == board[4] == board[7] and board[1] != ' ') or \
       (board[2] == board[5] == board[8] and board[2] != ' ') or \
       (board[3] == board[6] == board[9] and board[3] != ' ') or \
       (board[1] == board[5] == board[9] and board[5] != ' ') or \
       (board[3] == board[5] == board[7] and board[5] != ' '):
        Game = Win
    elif ' ' not in board[1:]:
        Game = Draw
    else:
        Game = Running

def intro():
    print("Hello! Welcome to X O game!")
    print("I'm sure you know the rules")
    print("""
    Select a game mode:
    1. Player vs Player
    2. Player vs Robot
    """)
    choice = input("Enter 1 or 2 to select a mode: ")
    if choice == '1':
        return 'player_vs_player'
    elif choice == '2':
        return 'player_vs_robot'
    else:
        print("Invalid selection, defaulting to Player vs Player.")
        return 'player_vs_player'

def check_position(x):
    return board[x] == ' '

def start_game():
    global player, select, Game, board
    while Game == Running:
        DrawBoard()
        if player % 2 != 0:
            print("Player 1's turn (X)")
            select = 'X'
        else:
            print("Player 2's turn (O)")
            select = 'O'

        try:
            choice = int(input("Enter the position between [1-9]: "))
            if choice < 1 or choice > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if check_position(choice):
            board[choice] = select
            player += 1
            logika()
        else:
            print("Position already taken, try again.")
            
        if Game == Win:
            DrawBoard()
            print(f"Player {player % 2 + 1} wins!")
            break
        elif Game == Draw:
            DrawBoard()
            print("It's a draw!")
            break

def vsrobot():
    global player, select, Game, board
    while Game == Running:
        DrawBoard()
        if player % 2 != 0:
            print("Player 1's turn (X)")
            select = 'X'
            try:
                choice = int(input("Enter the position between [1-9]: "))
                if choice < 1 or choice > 9:
                    print("Invalid input! Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
        else:
            print("Player 2's turn (O) - Robot")
            select = 'O'
            available_positions = [i for i in range(1, 10) if board[i] == ' ']
            choice = random.choice(available_positions)
            print(f"Robot chooses position {choice}")

        if check_position(choice):
            board[choice] = select
            player += 1
            logika()
        else:
            print("Position already taken, try again.")
            
        if Game == Win:
            DrawBoard()
            print(f"Player {player % 2 + 1} wins!")
            break
        elif Game == Draw:
            DrawBoard()
            print("It's a draw!")
            break

def main():
    game_mode = intro()
    if game_mode == 'player_vs_player':
        start_game()
    elif game_mode == 'player_vs_robot':
        vsrobot()

if __name__ == "__main__":
    main()
