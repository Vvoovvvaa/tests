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
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win                                  
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Running


def intro():
    print("Hello! Welcome to X O game!")
    print("\n")
    print("I'm sure you know the rules")
    print("\n")
    input("Press enter to continue.")
    print("\n")

def check_position(choice):
    if board[choice] == ' ':
        return True
    else:
        return False
    
def start_game():
    while Game == Running:
        DrawBoard()

    if player % 2 != 0:
        print("Player 1 chanche")
        select
    else:
        print("Player 2 chance")
        select
    choice = int(input("Enter the position between [1-9]: "))
    if check_position(choice):
        board[choice] == select  
        player += 1
        DrawBoard()

def main():
    intr = intro()
    boards = DrawBoard()
    logik = logika()
    pos = check_position()
    start = start_game()

if __name__=="__main__":
     main()







