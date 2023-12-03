def validate_game(max_red, max_green, max_blue, game_reveal):
	individual_reveals = game_reveal.split(";")
	for reveal in individual_reveals:
		cube_counts = reveal.split(", ")
		for count in cube_counts:
			count_dict = count.split()
			match count_dict[1]:
				case "red":
					if int(count_dict[0]) > max_red:
						return False
				case "green":
					if int(count_dict[0]) > max_green:
						return False
				case "blue":
					if int(count_dict[0]) > max_blue:
						return False
				case _:
					return False
	return True

def determine_min_power(game_reveal):
	max_red = max_green = max_blue = 0
	individual_reveals = game_reveal.split(";")
	for reveal in individual_reveals:
		cube_counts = reveal.split(", ")
		for count in cube_counts:
			count_dict = count.split()
			match count_dict[1]:
				case "red":
					max_red = max(int(count_dict[0]), max_red)
				case "green":
					max_green = max(int(count_dict[0]), max_green)
				case "blue":
					max_blue = max(int(count_dict[0]), max_blue)
				case _:
					return 0
	return max_red * max_green * max_blue


def part_one(input_array):
	total = 0
	for line in input_array:
		game_split = line.split(": ")
		game_id = game_split[0].split()[1]
		if validate_game(12,13,14,game_split[1]):
			total += int(game_id)
	print("Day 2, Part 1 Solution: " + str(total))

def part_two(input_array):
	total = 0
	for line in input_array:
		game_split = line.split(": ")
		total += determine_min_power(game_split[1])
	print("Day 2, Part 1 Solution: " + str(total))