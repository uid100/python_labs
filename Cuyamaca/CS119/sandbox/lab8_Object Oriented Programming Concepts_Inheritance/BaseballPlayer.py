#!/usr/bin/env python3

# lab 8 ex 3 Baseball Player class implementation

from Player import Player

class BaseballPlayer(Player):
    _POSITIONS = [ #"infield", "outfield", "battery", "bench" ]
        'reserved',
        'pitcher',
        'catcher',
        'first baseman',
        'second baseman',
        'third baseman',
        'shortstop',
        'left fielder',
        'center fielder',
        'right fielder',
        'outfielder',
        'coach',
        'manager',
        'designated hitter',
        'pinch hitter',
        'pinch runner',
        'utility infielder',
        'mascot'
    ]

    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)
        #self._batting_avg = batting_avg
        self.set_batting_avg(batting_avg)
        self.set_position(position)

    def get_position(self):
        return self._position
    def set_position(self, position):
        if position.lower() in BaseballPlayer._POSITIONS:
            self._position = position
        else:
            self._position = 'bench'

    def get_batting_avg(self):
        return self._batting_avg
    def set_batting_avg(self, avg):
        if avg > 0 and avg < 1:
            self._batting_avg = avg
        elif avg > 1 and avg < 1000:
            self._batting_avg = avg/1000.0
        else:
            self._batting_avg = 0.0

    def to_string(self):
        return f"{super().to_string():22}" + f" - {self._position} ({self._batting_avg:.3f})"

##### Unit Test #####
if __name__=="__main__":
    BaseballTeam = ('''
        {
            "Team": [
                {
                    "name": "Babe Ruth",
                    "nickname": "The Bambino",
                    "number": 3,
                    "position": "outfielder",
                    "batting average": 0.342
                },
                {
                    "name": "Randy Johnson",
                    "nickname": "The Big Unit",
                    "team": "Diamondbacks",
                    "number": 51,
                    "position": "pitcher",
                    "batting average": 0.125
                },
                {
                    "name": "Rob Picciolo",
                    "nickname": "Peach",
                    "team": "Padres",
                    "number": 5,
                    "position": "shortstop",
                    "batting average": 0.234
                },
                {
                    "name": "Bat_Avg Test",
                    "nickname": "Too High",
                    "team": "Cane Fires",
                    "number": 99,
                    "position": "pitcher",
                    "batting average": 303
                }
            ]
        }
    ''')


    import json
    team = json.loads(BaseballTeam)

    for p in team['Team']:
        ball_player = BaseballPlayer(p['name'],p['number'],p['position'],p['batting average'])
        print( ball_player.to_string() )
