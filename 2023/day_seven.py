from enum import Enum
class HandType(Enum):
	HIGH_CARD = 1
	ONE_PAIR = 2
	TWO_PAIR = 3
	THREE_KIND = 4
	FULL_HOUSE = 5
	FOUR_KIND = 6
	FIVE_KIND = 7

class CamelCardHand:
	hand = []
	score_type = None
	rank = -1
	bid = 0

	def __init__(self,cards, bid):
		self.hand = cards
		self.bid = bid

def is_five_kind(check_hand):
	return check_hand.count(check_hand[0]) == 5

def is_four_kind(check_hand):
	if check_hand.count(check_hand[0]) == 4:
		return True
	else:
		return check_hand.count(check_hand[1]) == 4


