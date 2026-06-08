class HandRanking:
    hands_by_Rank = {
        1: "AA", 2: "KK", 3: "QQ", 4: "JJ", 5: "TT",
    6: "99", 7: "88", 8: "AKs", 9: "77", 10: "AQs",
    11: "AJs", 12: "AKo", 13: "ATs", 14: "AQo", 15: "KQs",
    16: "66", 17: "AJo", 18: "A9s", 19: "KJs", 20: "ATo",
    21: "A8s", 22: "KQo", 23: "KTs", 24: "A7s", 25: "A9o",
    26: "55", 27: "A5s", 28: "KJo", 29: "A6s", 30: "QJs",
    31: "KTo", 32: "A4s", 33: "A3s", 34: "K9s", 35: "A8o",
    36: "A2s", 37: "QTs", 38: "A7o", 39: "QJo", 40: "44",
    41: "K8s", 42: "A6o", 43: "A5o", 44: "JTs", 45: "A4o",
    46: "QTo", 47: "K7s", 48: "A3o", 49: "A2o", 50: "Q9s",
    51: "K9o", 52: "33", 53: "T9s", 54: "J9s", 55: "JTo",
    56: "K6s", 57: "K8o", 58: "Q8s", 59: "K5s", 60: "Q9o",
    61: "J8s", 62: "K7o", 63: "T8s", 64: "K4s", 65: "T9o",
    66: "Q7s", 67: "J9o", 68: "K3s", 69: "Q6s", 70: "22",
    71: "K6o", 72: "98s", 73: "K2s", 74: "Q5s", 75: "Q8o",
    76: "K5o", 77: "J7s", 78: "T7s", 79: "Q4s", 80: "K4o",
    81: "T8o", 82: "Q3s", 83: "J8o", 84: "98o", 85: "87s",
    86: "Q7o", 87: "K3o", 88: "Q2s", 89: "Q6o", 90: "J6s",
    91: "97s", 92: "T6s", 93: "Q5o", 94: "K2o", 95: "J5s",
    96: "T7o", 97: "76s", 98: "J7o", 99: "Q4o", 100: "87o",
    101: "J4s", 102: "Q3o", 103: "86s", 104: "J3s", 105: "97o",
    106: "65s", 107: "T5s", 108: "J6o", 109: "T6o", 110: "Q2o",
    111: "J2s", 112: "75s", 113: "T4s", 114: "76o", 115: "J5o",
    116: "96s", 117: "86o", 118: "54s", 119: "T3s", 120: "T2s",
    121: "85s", 122: "J4o", 123: "65o", 124: "64s", 125: "75o",
    126: "J3o", 127: "95s", 128: "T5o", 129: "53s", 130: "84s",
    131: "J2o", 132: "T4o", 133: "74s", 134: "85o", 135: "63s",
    136: "54o", 137: "T3o", 138: "94s", 139: "64o", 140: "T2o",
    141: "52s", 142: "95o", 143: "73s", 144: "43s", 145: "53o",
    146: "84o", 147: "93s", 148: "62s", 149: "74o", 150: "96o",
    151: "92s", 152: "63o", 153: "82s", 154: "94o", 155: "52o",
    156: "42s", 157: "32s", 158: "43o", 159: "73o", 160: "93o",
    161: "83s", 162: "62o", 163: "72s", 164: "82o", 165: "92o",
    166: "42o", 167: "32o", 168: "83o", 169: "72o",
    }

    def __init__(self):
        self.rank_by_Hand = {self.hands_by_Rank[rank]: rank for rank in range(1, 170)} #dictionary of hand to rank
        self.combo_count_dict = {hand: self.combo_count_func(hand) for hand in self.rank_by_Hand.keys()}

    @staticmethod
    def combo_count_func(hand): #function to count the number of combos for a given hand
        return 6 if hand[0] == hand[1] else 12 if hand[2] == 'o' else 4

    def hand_rank(self, hand):
        return self.rank_by_Hand[hand]



