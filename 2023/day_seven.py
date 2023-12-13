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
	
def is_full_house(check_hand):
	first_label = ''
	second_label = ''
	first_label_count = 0
	second_label_count = 0
	for card in check_hand:
		if first_label == '':
			first_label = card
			first_label_count += 1
		elif card == first_label:
			first_label_count += 1
		elif second_label == '':
			second_label = card
			second_label_count += 1
		elif card == second_label:
			second_label_count += 1
		else:
			return False
	if first_label_count > 1 and second_label_count > 1:
		return True

def is_three_kind(check_hand):
	if check_hand.count(check_hand[0]) == 3:
		return True
	elif check_hand.count(check_hand[1]) == 3:
		return True
	else:
		return check_hand.count(check_hand[2]) == 3
	
def is_two_pair(check_hand):
	occurrences = dict()
	for card in check_hand:
		if occurrences.get(card) != None:
			occurrences[card] += 1
		else:
			occurrences[card] = 1
	pairs = 0
	for occurence in occurrences:
		if occurrences[occurence] == 2:
			pairs += 1
	return pairs == 2

def is_one_pair(check_hand):
	occurrences = dict()
	for card in check_hand:
		if occurrences.get(card) != None:
			occurrences[card] += 1
		else:
			occurrences[card] = 1
	pairs = 0
	for occurence in occurrences:
		if occurrences[occurence] == 2:
			pairs += 1
	return pairs == 1

def set_hand_type(camel_card_hand):
	if is_five_kind(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.FIVE_KIND
		return
	elif is_four_kind(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.FOUR_KIND
		return
	elif is_full_house(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.FULL_HOUSE
		return
	elif is_three_kind(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.THREE_KIND
		return
	elif is_two_pair(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.TWO_PAIR
		return
	elif is_one_pair(camel_card_hand.hand):
		camel_card_hand.score_type = HandType.ONE_PAIR
		return
	else:
		camel_card_hand.score_type = HandType.HIGH_CARD
