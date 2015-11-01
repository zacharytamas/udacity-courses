#
# In the first Lesson of the class we are attempting to
# build a Poker program.
#

def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  return max(hands, key=hand_rank)


def hand_rank(hand):
  "Return a value indicating the rank of a hand."
  ranks = card_ranks(hand)

  if straight(ranks) and flush(hand):            # straight flush
    return (8, max(ranks))
  elif kind(4, ranks):                           # 4 of a kind
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):        # full house
    return # your code here
  elif flush(hand):                              # flush
    return # your code here
  elif straight(ranks):                          # straight
    return # your code here
  elif kind(3, ranks):                           # 3 of a kind
    return # your code here
  elif two_pair(ranks):                          # 2 pair
    return # your code here
  elif kind(2, ranks):                           # kind
    return # your code here
  else:                                          # high card
    return # your code here


def card_ranks(hand):
  pass


def test():
  "Test cases for the functions in poker program"
  sf = "6C 7C 8C 9C TC".split()
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  assert poker([sf, fk, fh]) == sf
  assert poker([fk, fh]) == fk
  assert poker([fh, fh]) == fh
  assert poker([fh]) == fh
  assert poker([sf] + 99 * [fh]) == sf
  assert hand_rank(sf) == (8, 10)
  assert hand_rank(fk) == (7, 9, 7)
  assert hand_rank(fh) == (6, 10, 7)
  return 'tests pass'

print test()
