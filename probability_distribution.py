import math


class EquityCalculator:
    total_combos = 50*49/2 #total number of possible hands C(50,2) = 1225

    def __init__(self, hand_ranking):
        self.hand_ranking = hand_ranking

    def find_winning_combos(self, hand, rating, countlog, ranktohand):
        user_ranks = (hand[0], hand[1]) #number value of 2 cards in user's hand
        user_is_suited = (hand[0] != hand[1] and hand[2] == "s") #true if user's hand is suited

        counter = 0
        for i in range(1, rating):       #loop through all hands stronger than the user's hand
            stronger = ranktohand[i]          #hand string of the stronger hand
            x, y = stronger[0], stronger[1]       # number value of 2 cards in stronger hand [we know x >= y]

            nx = user_ranks.count(x) #number of cards in user's hand with rank x
            ny = user_ranks.count(y) #number of cards in user's hand with rank y


            if nx == 0 and ny == 0:
                counter += countlog[stronger]
                continue


            a, b = 4 - nx, 4 - ny   #important variables: both are number of cards in the deck left with rank x or y

            if x == y:
                # Stronger class is a pair sharing the user's rank.
                # surviving combos = C(a, 2)
                # Only reachable when the user is NOT a pair (a stronger pair can't share a pair-user's rank. That would be a tie, not a win).
                #   non-pair user shares the rank: a = 3 -> 6 becomes 3
                counter += a * (a - 1) // 2
            else:
                # Non-pair stronger class. We need s = the number of suits in which
                # BOTH ranks are still available:
                #   share one rank as a lone card ........ s = 3   (nx or ny == 1)
                #   share one rank as the user's pair .... s = 2   (nx or ny == 2)
                #   share both ranks, user offsuit ....... s = 2
                #   share both ranks, user suited ........ s = 3
                if nx == 1 and ny == 1 and user_is_suited:
                    s = 3
                else:
                    s = 4 - (nx + ny)

                if stronger[2] == "s":
                    # suited: combos = s
                    #   one shared rank   -> 4 becomes 3
                    #   pair-user's rank  -> 4 becomes 2
                    #   both ranks (offs) -> 4 becomes 2   (offsuit user's suited cousin)
                    counter += s
                else:
                    # offsuit: combos = a*b - s
                    #   one shared rank   -> 12 becomes 9
                    #   pair-user's rank  -> 12 becomes 6
                    counter += a * b - s

        return counter


    def probability_opponent_beats(self, hand):
        rank = self.hand_ranking.hand_rank(hand)
        stronger = self.find_winning_combos(hand, rank, self.hand_ranking.combo_count_dict, self.hand_ranking.hands_by_Rank)
        return stronger / self.total_combos


    def standing_distribution(self, p, num_players):
        opponents = num_players - 1
        distribution = []
        for i in range(num_players):
            distribution.append(math.comb(opponents, i) * (p ** i) * ((1 - p) ** (opponents - i)))
        return distribution

