import board.board as board
import board.locations as location
import parameters
import players
import tokens

def start():
    print("Tic-Tac-Toe")
    try:
        new_board = board.Board()
        new_board.make_board(parameters.gridsize)

        new_locations = location.Locations()
        new_locations.set_cell_locations(parameters.locations)
        new_locations.set_winning_combo(parameters.winning_combo)

        token1 = tokens.Token()
        player1 = players.Player()
        player1.set_id(parameters.player1)
        token1.setType(player1.get_id())
        player1.set_token(token1)

        token2 = tokens.Token()
        player2 = players.Player()
        player2.set_id(parameters.player2)
        token2.setType(player2.get_id())
        player2.set_token(token2)
    except Exception as e:
        print('Error: ', e)
        exit(-1)
    new_board.draw_board()

    won = False
    current_player = 1
    while won is False:
        if current_player == player1.get_id():
            player_input = input('Player 1: Choose a cell in row,column format.\n')
        else:
            player_input = input('Player 2: Choose a cell in row,column format.\n')
        player_input = player_input.replace(" ","")
        remove_check = new_locations.remove_cell(player_input)
        while remove_check is False:
            player_input = input('Invalid or location chosen already. Choose a cell in row,column format.\n')
            player_input = player_input.replace(" ", '')
            remove_check = new_locations.remove_cell(player_input)
        if current_player == player1.get_id():
            new_board.set_board(token1.getType(),player_input)
            player1.set_player_choices(player_input)
            new_board.draw_board()
            won = new_locations.win_check(player1.get_player_choices())
            current_player = player2.get_id()
        else:
            new_board.set_board(token2.getType(), player_input)
            player2.set_player_choices(player_input)
            new_board.draw_board()
            won = new_locations.win_check(player2.get_player_choices())
            current_player = player1.get_id()
        if won is True:
            print('Wow you won?!')
            again = input('Wanna play again? Y or N\n')
            if again.upper() == 'Y' or again.upper() == 'YES':
                start()
            elif again.upper() == 'N' or again.upper() == 'NO':
                print('Peace dawg.')
                exit(0)

if __name__ == "__main__":
    start()