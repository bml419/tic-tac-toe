locations = ['0,0','0,1','0,2','1,0','1,1','1,2','2,0','2,1','2,2']
winning_comb = [['0,0','1,1','2,2']]

def remove_cell(cell):
    if cell not in locations:
        return 1
    else:
        locations.remove(cell)
        return 0

def win_check():
    return 0