X = "X";
O = "O";
EMPTY = " ";
SIzE = 9;

turn = "";
human = "";
computer = "";

def main():
    if(yes_no"Would you like to go first?") == "y"):
        human = X;
        computer = O;
        turn = human;
    else:
        human = O;
        computer = X;
        turn = computer;
        board = [];
        setup_board(board);
        showInstructions();
        isInGame = inGame(board);
        while (isInGame):
            takeTurns(turn, board, human, computer);
            drawBoard(board, human, computer);
            if(checkWin(board,human, computer) == "human"):
                print("\n"+win("human))
                break;
            elif (checkWin(board, human, computer) == "computer"):
                print("\n"+win("computer"));
                break;
            turn = switchTurn(turn, human, computer);
            temp = inGame(board);
            if (temp == "yes"):
                isInGame - "yes";
            else:
                break;
            return "";
