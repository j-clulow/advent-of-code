translation_array = (["one","o1e"],["two","t2o"],["three","t3e"],["four","4"],["five","5e"],["six","6"],["seven","7"],["eight","e8t"],["nine","9e"])

def get_number(calibration_line):
	first_digit = 0
	second_digit = 0
	digit_found = False
	for char in enumerate(calibration_line):
		if char[1].isdigit():
			if not digit_found:
				first_digit = char[1]
				digit_found = True
			second_digit = char[1]
	return int(first_digit) *10 + int(second_digit)

def letters_to_numbers(calibration_line):
	for entry in translation_array:
		calibration_line = calibration_line.replace(str(entry[0]), str(entry[1]))
	return calibration_line

def part_one(input_array):
	total = 0
	for entry in input_array:
		total += get_number(entry)
	print("Day 1, Part 1 Solution: " + str(total))

def part_two(input_array):
	total = 0
	for entry in input_array:
		translated = letters_to_numbers(entry)
		total += get_number(translated)
	print("Day 1, Part 2 Solution: " + str(total))