def get_winning_numbers(card_info):
	numbers = list(set(card_info.split(': ')[1].split(' | ')[0].split(' ')))
	while numbers.count(''):
		numbers.remove('')
	return numbers

def get_card_numbers(card_info):
	numbers =  list(set(card_info.split(': ')[1].split(' | ')[1].split(' ')))
	while numbers.count(''):
		numbers.remove('')
	return numbers

def calculate_score(winning_numbers, card_numbers):
	matches = sum(num in card_numbers for num in winning_numbers)
	if matches > 0:

		return pow(2,matches-1)
	else:
		return 0

def part_one(pile):
	total_score = 0
	count = 1
	for card in pile:
		winning_numbers = get_winning_numbers(card)
		card_numbers = get_card_numbers(card)
		card_score = calculate_score(winning_numbers, card_numbers)
		print("Card " + str(count) + ": " + str(card_score))
		print(winning_numbers)
		print(card_numbers)
		total_score += card_score
		count += 1
	print("Solution for Day 4, Part 1: " + str(int(total_score)))