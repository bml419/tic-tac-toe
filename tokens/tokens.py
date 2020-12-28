class Token():
    def __init__(self):
        self.type = ''

    # id getter
    def getType(self):
        return self.type
    # id setter
    def setType(self, id):
        if id == 1:
            self.type = 'X'
        elif id == 2:
            self.type = 'O'

