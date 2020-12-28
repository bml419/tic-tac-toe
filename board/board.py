class Board:
    def __init__(self):
        self.board_spaces = []

    def make_board(self, gridsize):
        for i in range(gridsize*gridsize):
            self.board_spaces.append(' ')

    def set_board(self, token, input):
        if str(input) == '0,0':
            self.board_spaces[0] = token
        elif str(input) == '0,1':
            self.board_spaces[1] = token
        elif str(input) == '0,2':
            self.board_spaces[2] = token
        elif str(input) == '1,0':
            self.board_spaces[3] = token
        elif str(input) == '1,1':
            self.board_spaces[4] = token
        elif str(input) == '1,2':
            self.board_spaces[5] = token
        elif str(input) == '2,0':
            self.board_spaces[6] = token
        elif str(input) == '2,1':
            self.board_spaces[7] = token
        elif str(input) == '2,2':
            self.board_spaces[8] = token

    def draw_board(self):
        print('   0     1    2')
        print('0' + '  ' + self.board_spaces[0] + '  |  ' + self.board_spaces[1] + '  |  ' + self.board_spaces[2])
        print('  ----+-----+----')
        print('1' + '  ' + self.board_spaces[3] + '  |  ' + self.board_spaces[4] + '  |  ' + self.board_spaces[5])
        print('  ----+-----+----')
        print('2' + '  ' + self.board_spaces[6] + '  |  ' + self.board_spaces[7] + '  |  ' + self.board_spaces[8])

'''
    def __str__(self):
        print('   0     1    2')
        print('0' + '  '+ self.board_spaces[0] + '  |  ' + self.board_spaces[1] + '  |  ' + self.board_spaces[2])
        print('  ----+-----+----')
        print('1' + '  '+ self.board_spaces[3] + '  |  ' + self.board_spaces[4] + '  |  ' + self.board_spaces[5])
        print('  ----+-----+----')
        print('2' + '  '+ self.board_spaces[6] + '  |  ' + self.board_spaces[7] + '  |  ' + self.board_spaces[8])
'''




