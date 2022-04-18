#!/usr/bin/env python3

# lab 8 ex 3 Basketball Player class implementation

from Player import Player

class BasketballPlayer(Player):
    _POSITIONS = [ 
        'point guard',
        'shooting guard',
        'small forward',
        'power forward',
        'center'
    ]

    def __init__(self, name, number, position, free_throw_percentage):
        super().__init__(name, number)
        self._free_throw_percentage = free_throw_percentage
        self.set_position(position)

    def get_position(self):
        return self._position
    def set_position(self, position):
        if position.lower() in BasketballPlayer._POSITIONS:
            self._position = position
        else:
            self._position = 'bench'

    def get_free_throw_percentage(self):
        return self._free_throw_percentage
    def set_free_throw_percentage(self, free_throw):
        if free_throw > 1 and free_throw <= 100:
            self._free_throw_percentage = free_throw
        elif free_throw > 0 and free_throw <= 1:
            self._free_throw_percentage = free_throw * 100
        else:
            self._free_throw_percentage = 0.0

    def to_string(self):
        return f"{super().to_string():22}" + f" - {self._position} ({self._free_throw_percentage:.1f})"

##### Unit Test #####
if __name__=="__main__":
    Squad = ('''
        {
            "Team": [
                {
                    "name": "Earvin Johnson",
                    "nickname": "Magic",
                    "number": 32,
                    "position": "point guard",
                    "team": "lakers",
                    "free throw percentage": 91.1
                },
                {
                    "name": "Wilt Chamberlain",
                    "nickname": "Wilt The Stilt",
                    "team": "Lakers",
                    "number": 13,
                    "position": "point guard",
                    "free throw percentage": 87.5
                },
                {
                    "name": "Shaquile O'Neal",
                    "nickname": "Shaq",
                    "team": "Heat",
                    "number": 34,
                    "position": "point guard",
                    "free throw percentage": 52.7
                }
            ]
        }
    ''')


    import json
    team = json.loads(Squad)

    for p in team['Team']:
        ball_player = BasketballPlayer(p['name'],p['number'],p['position'],p['free throw percentage'])
        print( ball_player.to_string() )
