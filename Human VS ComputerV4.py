while True:

    import os
    import time 
    import random 

    #define the board 
    board = [""," "," "," "," "," "," "," "," "," "]

    #define the print_board function 
    def print_header():
    	print("""
                _____  _  ____     _____  ____  ____     _____  ____  _____
               /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
                 / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      
                 | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
                 \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\
                                                                            
                 To play Tic-Tac-Toe, you need to get three in a row...
                 Your choices are defined, they must be from 1 to 9...

    """)

    #Define the print_board function
    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
        print("   |   |   ")
        
        
    def is_winner(board, player):
        if(board[1] == player and board[2] == player and board[3] == player) or\
            (board[4] == player and board[5] == player and board[6] == player)or\
            (board[7] == player and board[8] == player and board[9] == player)or\
            (board[1] == player and board[4] == player and board[7] == player)or\
            (board[2] == player and board[5] == player and board[8] == player)or\
            (board[3] == player and board[6] == player and board[9] == player)or\
            (board[1] == player and board[5] == player and board[9] == player)or\
            (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True
            
    def get_computer_move(board, player):

        it = play_defense(board, player)
        if it:
            return it
        
        #check colums for a win 
        for i in range(1,10):
            if board[i] == " ":
                board [i] = player
                if is_winner(board, player):
                    return i
                else:
                    board[i] = " "
       
        #lists for better first moves.
        cornerDefense = [1,3,7,9]
        cornersFull = [1,3,7,9]
        edges = [2,4,6,8]
        #if center square is empty choose that.
        if board[5] == " ":
            return 5
        elif board[5] == "X":
            return random.choice(cornerDefense)

        elif cornersFull == player:
            return random.choice(edges)
        #ultimate human play
        for i in [1]:
            if board[i+4] == "O" and board[i+8] == "X" and board[i+4] == "X":
                return random.choice(cornerDefense)
            if board[i+4] == "O" and board[i+6] == "X" and board[i+1] == "X":
                return random.choice(cornerDefense)
            if board[i+4] == "O" and board[i] == "X" and board[i+5] == "X":
                return random.choice(cornerDefense)
            if board[i+4] == "O" and board[i+2] == "X" and board[i+7] == "X":
                return random.choice(cornerDefense)

        while True:
            move = random.randint(1,9)
            # move is blank go and return otherwise try again
            if board[move] == " ":
                return move
        """
        beatable positions are 9,4  7,2  1,6  3,8 must go to availiable corner to block.
        """

    def play_defense(board, player):
        
        #columns
        for i in [1,2,3]:
            if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                return i+6
            if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                return i+3
        #rows
        for a in [1,4,7]:
            if board[a] == "X" and board[a+1] == "X" and board[a+2] == " ":
                return a+2
            if board[a+1] == "X" and board[a+2] == "X" and board[a] == " ":
                return a
            if board[a+2] == "X" and board[a] == "X" and board[a+1] == " ":
                return a+1

        if board[1] == "X" and board[5] == "X" and board[9] == " ":
           return 9	
        if board[5] == "X" and board[9] == "X" and board[1] == " ":
           return 1	
        if board[9] == "X" and board[1] == "X" and board[5] == " ":
           return 5	

        if board[3] == "X" and board[5] == "X" and board[7] == " ":
           return 7
        if board[5] == "X" and board[7] == "X" and board[3] == " ":
           return 3
        if board[7] == "X" and board[3] == "X" and board[5] == " ":
           return 5
                
    while True:
        os.system("clear")
        print_header()
        print_board()
        
        #Get player X input
        choice = input("please choose an empty space for X (YOU ARE X). ")
        choice = int(choice)
        
        #check to see if space is empty first
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Sorry,that space is not empty!")
            time.sleep(1)
        
        #check for X win
        if is_winner(board, "X"):
            os.system("clear")
            print_header()
            print_board()
            print("X wins! congrats")
            break
         
        os.system("clear")
        print_header()
        print_board()
         
         #check for tie in the board 
         #if board is full do something 
        if is_board_full(board):
            os.system("clear")
            print_header()
            print_board()
            print("Tie!")
            break
             
         #get player O  Input
        choice = get_computer_move(board, "O")
        
        #check to see if space is empty first
        if board[choice] == " ":
            board[choice] ="O"
        else:
            print("Sorry,that space is not empty!")
            time.sleep(1)
        
        #check for O win
        if is_winner(board, "O"):
            os.system("clear")
            print_header()
            print_board()
            print("computer won, you lose :( ")
            break
        

        #if board is full do something 
        if is_board_full(board):
            print("Tie!")
            break

    user_resp=input(" \nWould you like to play again? \n\n y or n")
    if user_resp=="y":
            user_resp=1
    elif user_resp=="n":
            break
