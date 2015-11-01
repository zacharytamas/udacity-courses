#
# In the first Lesson of the class we are attempting to
# build a Poker program.
#

def poker(hands):
  "Return the best hand: poker([hand,...]) => hand"
  return max(hands, key=hand_rank)


def hand_rank(hand):
  return hand
