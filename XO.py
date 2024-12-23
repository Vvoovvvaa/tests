import random

board = [' '] * 10
player = 1
Game = 0  

def draw_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")

def check_winner():
    global Game
    win_positions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] != ' ':
            Game = 1
            return
    if ' ' not in board[1:]:
        Game = -1

def is_position_free(pos):
    return board[pos] == ' '

def player_move():
    while True:
        try:
            pos = int(input("Enter a position (1-9): "))
            if pos < 1 or pos > 9:
                print("Invalid position! Choose between 1 and 9.")
            elif not is_position_free(pos):
                print("Position already taken. Try another one.")
            else:
                return pos
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def robot_move():
    available_positions = [i for i in range(1, 10) if is_position_free(i)]
    return random.choice(available_positions)

def play_game(is_robot):
    global player, Game, board
    while Game == 0:
        draw_board()
        print(f"Player {player}'s turn ({'X' if player == 1 else 'O'})")
        if is_robot and player == 2:
            pos = robot_move()
            print(f"Robot chooses position {pos}")
        else:
            pos = player_move()
        board[pos] = 'X' if player == 1 else 'O'
        check_winner()
        if Game == 1:
            draw_board()
            print(f"Player {player} wins!")
        elif Game == -1:
            draw_board()
            print("It's a draw!")
        player = 3 - player 

def main():
    print("Welcome to Tic Tac Toe!")
    print("Choose game mode:")
    print("1. Player vs Player")
    print("2. Player vs Robot")
    while True:
        mode = input("Enter 1 or 2: ")
        if mode in ['1', '2']:
            break
        print("Invalid choice. Enter 1 or 2.")
    play_game(is_robot=(mode == '2'))

if __name__ == "__main__":
    main()
