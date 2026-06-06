def getNumPlayers(self):
    while True:
        numplayers = input("Type the number of players[must be between 2-10]: ")
        if int(numplayers) < 10 and int(numplayers) >1:
            return numplayers
def getCards(self):
    c1 = input("Type your first card(Ah is Ace of hearts): ")
    c2 = input("Type your second card: ")
    return c1+c2




