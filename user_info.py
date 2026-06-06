def getNumPlayers(self):
    while True:
        numplayers = input("Type the number of players[must be between 2-10]: ")
        if int(numplayers) < 10 and int(numplayers) >1:
            return numplayers
def getCards(self):
    from handRankHeadsup import hands_ranked_headsup
    valid_combos = hands_ranked_headsup.keys()
    while True:
        combo = input("Type your hand combo (e.g. AKs, AKo, AA): ")
        if combo in valid_combos:
            return combo
        print(f"Invalid combo '{combo}'. Must be one of the 169 combos (e.g. AKs, AKo, AA).")




