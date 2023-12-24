player1=input("Enter the name of player one : ")
player2=input("Enter the name of player two : ")
print("When you are told choose the possition please enter the corresponding number to fill the possition you want as follows.")
print("1|2|3")
print("-|-|-")
print("4|5|6")
print("-|-|-")
print("7|8|9")
print()
print("-------------------")
print()

    
board={"1":" ","2":" ","3":" ",
      "4":" ","5":" ","6":" ",
      "7":" ","8":" ","9":" ",}

player=1
count_moves=0
win=False

def check_win():
    global win
    
    #Horizontal
    if (all(board[i]=="X" for i in ["1","2","3"])) or (all(board[i]=="X" for i in ["4","5","6"])) or (all(board[i]=="X" for i in ["7","8","9"])):
        print(f"{player1} won the game (Horizontal)")
        win=True
    if (all(board[i]=="O" for i in ["1","2","3"])) or (all(board[i]=="O" for i in ["4","5","6"])) or (all(board[i]=="O" for i in ["7","8","9"])):
        print(f"{player2} won the game (Horizontal)")
        win=True
    
    #Vertical
    if (all(board[i]=="X" for i in ["1","4","7"])) or (all(board[i]=="X" for i in ["2","5","8"])) or (all(board[i]=="X" for i in ["3","6","9"])):
        print(f"{player1} won the game (Vertical)")
        win=True
    if (all(board[i]=="O" for i in ["1","4","7"])) or (all(board[i]=="O" for i in ["2","5","8"])) or (all(board[i]=="O" for i in ["3","6","9"])):
        print(f"{player2} won the game (Vertical)")
        win=True
    
    #Diagonal
    if (all(board[i]=="X" for i in ["1","5","9"])) or (all(board[i]=="X" for i in ["3","5","7"])):
        print(f"{player1} won the game (Diagonal)")
        win=True
    if (all(board[i]=="O" for i in ["1","5","9"])) or (all(board[i]=="O" for i in ["3","5","7"])):
        print(f"{player2} won the game (Diagonal)")
        win=True

while True:
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
    print("-|-|-")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-|-|-")
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    
    check_win()
    
    if count_moves==9 or win:
        break
    while True:
        if player==1:
            p1=input(f"{player1}, choose the possition: ").upper()
            if (p1 in board) and (board[p1]==" "):
                board[p1]="X"
                player=2
                break
            else:
                print("Invalid position")
                continue
        else:
            p2=input(f"{player2}, choose the possition: ").upper()
            if (p2 in board) and (board[p2]==" "):
                board[p2]="O"
                player=1
                break
            else:
                print("Invalid position")
                continue
    count_moves+=1
    print()