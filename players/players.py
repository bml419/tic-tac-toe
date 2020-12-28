class Player:
    def __init__(self):
        self.__player_choices = []
        self.__id = None
        self.__token = ''


    def get_player_choices(self):
        return self.__player_choices

    def set_player_choices(self, location):
        self.__player_choices.append(location)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_token(self):
        return self.__id

    def set_token(self, new_token):
        self.__token = str(new_token)