from enum import Enum
from functools import cmp_to_key
from statistics import mode

class HandType(Enum):
	HIGH_CARD = 1
	ONE_PAIR = 2
	TWO_PAIR = 3
	THREE_KIND = 4
	FULL_HOUSE = 5
	FOUR_KIND = 6
	FIVE_KIND = 7

	def __eq__(self, other):
		if type(self) == type(other):
			return self.value == other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __lt__(self, other):
		if type(self) == type(other):
			return self.value < other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __gt__(self, other):
		if type(self) == type(other):
			return self.value > other.value
		else:
			raise('Cannot compare Enums of different classes.')

class CardLabel(Enum):
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14

	def __eq__(self, other):
		if type(self) == type(other):
			return self.value == other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __lt__(self, other):
		if type(self) == type(other):
			return self.value < other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __gt__(self, other):
		if type(self) == type(other):
			return self.value > other.value
		else:
			raise('Cannot compare Enums of different classes.')
		
class JokerisedCardLabel(Enum):
	JOKER = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	QUEEN = 11
	KING = 12
	ACE = 13

	def __eq__(self, other):
		if type(self) == type(other):
			return self.value == other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __lt__(self, other):
		if type(self) == type(other):
			return self.value < other.value
		else:
			raise('Cannot compare Enums of different classes.')
	def __gt__(self, other):
		if type(self) == type(other):
			return self.value > other.value
		else:
			raise('Cannot compare Enums of different classes.')

class CamelCardHand:
	hand = []
	score_type = None
	rank = -1
	bid = 0

	def __init__(self,cards, bid):
		self.hand = cards
		self.bid = bid
	

	def __eq__(self, other):
		if other == None:
			return False
		if self.score_type != other.score_type:
			return False
		for index in range(0,len(self.hand)):
			if self.hand[index] != other.hand[index]:
				return False
		return True
	
	def __gt__(self, other):
		if other == None:
			return False
		if self.score_type > other.score_type:
			return True
		elif self.score_type < other.score_type:
			return False
		else:
			for index in range(0,self.hand):
				if self.hand[index] == other.hand[index]:
					continue
				else:
					return self.hand[index] > other.hand[index]
		return False
	
	def __lt__(self, other):
		return not (self > other or self == other)
	
	def __str__(self):
		return 'Cards in Hand: {0}. Score Type is: {1}. Rank is :{2}. Bid at: {3}'.format(self.hand, self.score_type.name, self.rank, self.bid)
	
def compare_labels(label1, label2):
	if label1 < label2:
		return -1
	elif label1 > label2:
		return 1
	else:
		return 0
	
def compare_hands(hand1, hand2):
	if hand1.score_type < hand2.score_type:
		return -1
	elif hand1.score_type > hand2.score_type:
		return 1
	else:
		hand1_conv = convert_hand_to_labels(hand1.hand)
		hand2_conv = convert_hand_to_labels(hand2.hand)
		for index in range(0,len(hand1_conv)):
			result = compare_labels(hand1_conv[index],hand2_conv[index])
			if result == 0:
				continue
			else:
				return result
	return 1

def compare_hands(hand1, hand2):
	if hand1.score_type < hand2.score_type:
		return -1
	elif hand1.score_type > hand2.score_type:
		return 1
	else:
		hand1_conv = convert_hand_to_labels_joker(hand1.hand)
		hand2_conv = convert_hand_to_labels_joker(hand2.hand)
		for index in range(0,len(hand1_conv)):
			result = compare_labels(hand1_conv[index],hand2_conv[index])
			if result == 0:
				continue
			else:
				return result
	return 1

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

def handle_joker(hand):
	jokerless_hand = list(hand)
	while jokerless_hand.count('J')> 0:
		jokerless_hand.remove('J')
	if len(jokerless_hand) == 0:
		most_frequent = 'K'
	else:
		most_frequent = mode(jokerless_hand)
	jokered_hand = list(hand)
	for index in range(0,len(jokered_hand)):
		if jokered_hand[index] == 'J':
			jokered_hand[index] = str(most_frequent)
	return jokered_hand


def set_hand_type(camel_card_hand):
	processed_hand = list(camel_card_hand.hand)
	if processed_hand.count('J') > 0:
		processed_hand = handle_joker(processed_hand)
	if is_five_kind(processed_hand):
		camel_card_hand.score_type = HandType.FIVE_KIND
		return
	elif is_four_kind(processed_hand):
		camel_card_hand.score_type = HandType.FOUR_KIND
		return
	elif is_full_house(processed_hand):
		camel_card_hand.score_type = HandType.FULL_HOUSE
		return
	elif is_three_kind(processed_hand):
		camel_card_hand.score_type = HandType.THREE_KIND
		return
	elif is_two_pair(processed_hand):
		camel_card_hand.score_type = HandType.TWO_PAIR
		return
	elif is_one_pair(processed_hand):
		camel_card_hand.score_type = HandType.ONE_PAIR
		return
	else:
		camel_card_hand.score_type = HandType.HIGH_CARD
	
def convert_hand_to_labels(char_hand):
	conversions = {'2':CardLabel.TWO, '3':CardLabel.THREE, '4':CardLabel.FOUR, '5': CardLabel.FIVE,
				'6':CardLabel.SIX, '7':CardLabel.SEVEN, '8':CardLabel.EIGHT, '9':CardLabel.NINE,
				'T':CardLabel.TEN,'J':CardLabel.JACK, 'Q':CardLabel.QUEEN, 'K':CardLabel.KING,
				'A':CardLabel.ACE}
	label_hand = list()
	for index in range(0,len(char_hand)):
		label_hand.append(conversions[char_hand[index]])
	return label_hand

def convert_hand_to_labels_joker(char_hand):
	conversions = {'2':JokerisedCardLabel.TWO, '3':JokerisedCardLabel.THREE, '4':JokerisedCardLabel.FOUR,
				'5': JokerisedCardLabel.FIVE, '6':JokerisedCardLabel.SIX, '7':JokerisedCardLabel.SEVEN,
				'8':JokerisedCardLabel.EIGHT, '9':JokerisedCardLabel.NINE, 'T':JokerisedCardLabel.TEN,
				'J':JokerisedCardLabel.JOKER, 'Q':JokerisedCardLabel.QUEEN, 'K':JokerisedCardLabel.KING,
				'A':JokerisedCardLabel.ACE}
	label_hand = list()
	for index in range(0,len(char_hand)):
		label_hand.append(conversions[char_hand[index]])
	return label_hand

def part_one(hands):
	camel_card_hands = list()
	for item in hands:
		cards = list(item.split(' ')[0])
		bid = int(item.split(' ')[1])
		camel_card_hands.append(CamelCardHand(cards,bid))
	for camel_card_hand in camel_card_hands:
		set_hand_type(camel_card_hand)
	sorted_hands = sorted(camel_card_hands, key=cmp_to_key(compare_hands))
	rank = 1
	total_winnings = 0
	for hand in sorted_hands:
		hand.rank = rank
		total_winnings = total_winnings + (hand.bid*rank) 
		rank += 1
	print('Solution for Day 7 Part 1 is {0}'.format(total_winnings))

def part_two(hands):
	camel_card_hands = list()
	for item in hands:
		cards = list(item.split(' ')[0])
		bid = int(item.split(' ')[1])
		camel_card_hands.append(CamelCardHand(cards,bid))
	for camel_card_hand in camel_card_hands:
		set_hand_type(camel_card_hand)
	sorted_hands = sorted(camel_card_hands, key=cmp_to_key(compare_hands))
	rank = 1
	total_winnings = 0
	for hand in sorted_hands:
		hand.rank = rank
		total_winnings = total_winnings + (hand.bid*rank) 
		rank += 1
	print('Solution for Day 7 Part 2 is {0}'.format(total_winnings))
