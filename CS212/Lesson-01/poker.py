#
# In the first Lesson of the class we are attempting to
# build a Poker program.
#

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(hand))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks))
    elif kind(2, ranks):                           # kind
        return (1, ranks)
    else:                                          # high card
        return (0, ranks)


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."

    RANK_MAP = dict(zip(["T", "J", "Q", "K", "A"], range(10, 15)))

    def rank_to_int(card):
        r, s = card
        if r in RANK_MAP:
            return RANK_MAP[r]
        else:
            return int(r)

    ranks = map(rank_to_int, cards)
    ranks.sort(reverse=True)
    return ranks


def straight(ranks):
  "Return True if the ordered ranks form a 5-card straight."
  return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
  "Return True if all the cards have the same suit."
  suits = [s for r, s in hand]
  return len(set(suits)) == 1


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

print test()
