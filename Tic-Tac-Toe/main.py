# Imports
import parameters.config as conf
import board.board as b
import tokens as t
import board.locations as loc
import players as p

"""
main.py:
Will call start method to begin the game
"""

print("Tic-Tac-Toe")
print("Made by: Oscar Ortiz")

def main():
    board = b.makeboard(conf.gridsize)

    b.drawboard(board)
    #exit(0)
    won = 0
    player = 0
    player1 = []
    player2 = []
    #print(loc.locations)

    while won != 1:
        if player == 0:
            cell = input('Player One: Choose cell in row,column format.\n')
            token = t.getToken(player)
            flag = loc.remove_cell(cell)
            while flag == 1:
                cell = input('Player One: Location already chosen or invalid. Try again.\n')
                flag = loc.remove_cell(cell)
            b.setboard(token,cell,board)
            b.drawboard(board)
            list1 = p.addLoc(cell, player1)
            print('list for 1:', list1)
            won = loc.win_check(list1)
            if won == 1:
                print('Wow you won idiot!')
                again = input('Wanna play again? Y or N\n')
                if again == 'Y':
                    main()
                elif again == 'N':
                    print('Peace dawg.')
                    exit(0)
            player = 1
        elif player == 1:
            cell = input('Player Two: Choose cell in row,column format.\n')
            token = t.getToken(player)
            flag = loc.remove_cell(cell)
            while flag == 1:
                cell = input('Player One: Location already chosen or invalid. Try again.\n')
                flag = loc.remove_cell(cell)
            b.setboard(token, cell, board)
            b.drawboard(board)
            list2 = p.addLoc(cell,player2)
            print('list for 2:', list2)
            won = loc.win_check(list2)
            if won == 1:
                print('Wow you won idiot!')
                again = input('Wanna play again? Y or N\n')
                if again == 'Y':
                    main()
                elif again == 'N':
                    print('Peace dawg.')
                    exit(0)
            player = 0

main()