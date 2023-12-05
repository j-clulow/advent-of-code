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

def calculate_matches(winning_numbers, card_numbers):
	return sum(num in card_numbers for num in winning_numbers)

def calculate_score(winning_numbers, card_numbers):
	matches = calculate_matches(winning_numbers, card_numbers)
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
		total_score += card_score
		count += 1
	print("Solution for Day 4, Part 1: " + str(int(total_score)))

def part_two(pile):
	count = 1
	scratchcards = dict()
	for card in pile:
		scratchcards[str(count)] = 1
		count += 1
	count = 1
	for card in pile:
		winning_numbers = get_winning_numbers(card)
		card_numbers = get_card_numbers(card)
		card_matches = calculate_matches(winning_numbers, card_numbers)
		messages = []
		for index in range(count+1, count+card_matches+1):
			messages.append(("Adding " + str(scratchcards[str(count)]) + " copies of card " + str(index)))
			scratchcards[str(index)] += scratchcards[str(count)]
		count += 1
	print("Solution for Day 4, Part 2 is " + str(sum(scratchcards.values())))