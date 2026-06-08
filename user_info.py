class UserInput:
    def __init__(self, hand_ranking):
        self.hand_ranking = hand_ranking

    def get_num_players(self):
        while True:
            try:
                numplayers = int(input("Type the number of players[must be between 2-10]: "))
                if numplayers <= 10 and numplayers >1:
                    return numplayers
                else:
                    print("Invalid input. Please enter a number between 2 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 2 and 10.")

    def get_cards(self):
        valid_combos = self.hand_ranking.rank_by_Hand.keys()
        while True:   
            combo = input("Type your hand combo (e.g. AKs, QTo, 55) [bigger card first]: ")
            if combo in valid_combos:
                return combo
            print(f"Invalid combo '{combo}'. Must be one of the 169 combos (e.g. AKs, AKo, AA).") 




