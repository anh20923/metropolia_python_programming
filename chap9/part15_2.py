class Player:
    # __points = 0

    def __init__(self, teamcolor):
        self.teamcolor=teamcolor
        self.__points=0

    def tellscore(self):
        print(f"I am {self.teamcolor}, we have {self.__points} points!")

    def goal(self):
        self.__points += 1


player =Player("Blue")
player.goal()
player.tellscore()
