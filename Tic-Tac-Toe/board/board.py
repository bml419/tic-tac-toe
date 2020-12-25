"""
makeboard(gridsize):
Will create board for players to play on
"""


def makeboard(gridsize):
    boardspaces = []
    for i in range(gridsize*gridsize):
        boardspaces.append(' ')

    return boardspaces



def drawboard(boardspaces):

    print('   0     1    2')
    print('0' + '  '+ boardspaces[0] + '  |  ' + boardspaces[1] + '  |  ' + boardspaces[2])
    print('  ----+-----+----')
    print('1' + '  '+ boardspaces[3] + '  |  ' + boardspaces[4] + '  |  ' + boardspaces[5])
    print('  ----+-----+----')
    print('2' + '  '+ boardspaces[6] + '  |  ' + boardspaces[7] + '  |  ' + boardspaces[8])

def setboard(token,input,boardspaces):
    if str(input) == '0,0':
        boardspaces[0] = token
    elif str(input) == '0,1':
        boardspaces[1] = token
    elif str(input) == '0,2':
        boardspaces[2] = token
    elif str(input) == '1,0':
        boardspaces[3] = token
    elif str(input) == '1,1':
        boardspaces[4] = token
    elif str(input) == '1,2':
        boardspaces[5] = token
    elif str(input) == '2,0':
        boardspaces[6] = token
    elif str(input) == '2,1':
        boardspaces[7] = token
    elif str(input) == '2,2':
        boardspaces[8] = token









    #print(boardspaces)