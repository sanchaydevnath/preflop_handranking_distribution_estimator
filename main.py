from handRankHeadsup import HandRanking
from user_info import UserInput
from probability_distribution import EquityCalculator
from plotter import DistributionPlotter


class PreflopApp:
    def __init__(self):
        self.ranking = HandRanking()
        self.user_input = UserInput(self.ranking)
        self.calculator = EquityCalculator(self.ranking)
        self.plotter = DistributionPlotter()

    def run(self):
        num_players = self.user_input.get_num_players()
        user_cards = self.user_input.get_cards()
        beat_probability = self.calculator.probability_opponent_beats(user_cards)
        distribution = self.calculator.standing_distribution(beat_probability, num_players)
        self.plotter.plot(distribution, user_cards)


if __name__ == "__main__":
    PreflopApp().run()
