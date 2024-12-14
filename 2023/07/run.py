import sys
import re
import math

def analyze_hand(hand):
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    return "".join([ str(x) for x in reversed(sorted(cards.values())) ])

ORDER = "AKQJT98765432"
MAP = { card: chr(ord("A")+i) for i, card in enumerate(reversed(ORDER)) }
# print(f"{ORDER=} {MAP=}")
def main():
    result = 0
    path = "example"
    path = "input"
    hands = []
    with open(path, "r") as f:
        for line in f.readlines():
            if match := re.search("(.....) ([0-9]+)", line):
                hand = match.group(1)
                bid = int(match.group(2))
                key = analyze_hand(hand) + "".join([ MAP[card] for card in hand ])
                hands.append((key, bid))
                # print(f"{hand=} {bid=} {key=}")
    hands = sorted(hands)
    # print(hands)
    for i, (_, bid) in enumerate(hands):
        result += (i+1) * bid
    print(result)

    
if __name__ == "__main__": main()
