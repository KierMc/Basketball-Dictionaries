kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jayson = {
    "name": "Jayson Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },

    {
    "name": "Jayson Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },

    {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },

    {
    "name": "Damian Lillard", 
    "age":33,
        "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },

    {
    "name": "Joel Embiid", 
    "age":32,
        "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },

    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, player_dict):
        self.name=player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):
        return "Player: {}. {} y/o. pos: {}, team: {}".format(self.name, self.age, self.position, self.team)

player_kevin = Player(kevin)
print(player_kevin)

player_jayson = Player(jayson)
print(player_jayson)

player_kyrie = Player(kyrie)
print(player_kyrie)

new_team=[]
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)