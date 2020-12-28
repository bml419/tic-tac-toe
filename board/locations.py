class Locations:
    def __init__(self):
        self.cell_locations = []
        self.winning_combo = []

    def remove_cell(self,input):
        if input not in self.cell_locations:
            return False
        else:
            self.cell_locations.remove(input)
            return True

    def win_check(self,player_choices):
        for i in self.winning_combo:
            list_check = [value for value in i if value in player_choices]
            if len(list_check) == 3:
                return True
        return False

    def get_cell_locations(self):
        return self.cell_locations

    def set_cell_locations(self,locations):
        self.cell_locations = locations

    def get_winning_combo(self):
        return self.winning_combo

    def set_winning_combo(self,winning_list):
        self.winning_combo = winning_list
