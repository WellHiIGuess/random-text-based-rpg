import json


class Player:
    data = {}

    def __init__(self):
        with open('player_data.json', 'r') as f:
            self.data = json.loads(f.read())
            # print(self.data)
