class Player:
    def __init__(self, teamcolor, points):
        self.teamcolor=teamcolor
        self.points=points
player =Player("Blue", 300)
print(f"The {player.teamcolor} contender has {player.points} points!")
