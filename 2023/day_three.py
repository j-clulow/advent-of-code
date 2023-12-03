class SchematicPart:
	x = -1
	y = -1
	length = 0
	value = 0

	def __init__(self, x, y, len, val):
		self.x = x
		self.y = y
		self.length = len
		self.value = val

schematic_parts = []

def is_symbol(character):
	return not character.isalnum() and character != '.'

def is_x_boundary(x,schematic):
	return x >= len(schematic[0]) or x < 0

def is_y_boundary(y, schematic):
	return y >= len(schematic) or y < 0

def part_already_counted(x,y):
	return any(part.x == x and part.y == y for part in schematic_parts)

def process_schematic_part(x,y,schematic):
	temp_x = x
	number_string = ''
	while schematic[y][temp_x].isdigit():
		temp_x -= 1
		if is_x_boundary(temp_x, schematic):
			break
	start_x = temp_x + 1
	if part_already_counted(start_x,y):
		return
	temp_x = start_x
	while schematic[y][temp_x].isdigit():
		number_string += schematic[y][temp_x]
		temp_x += 1
		if is_x_boundary(temp_x, schematic):
			break
	schematic_parts.append(SchematicPart(start_x,y,temp_x-start_x,int(number_string)))
	

def adjacent_numbers(x,y,schematic):
	for x_adjust in range(-1,2):
		if is_x_boundary(x+x_adjust, schematic):
			continue
		for y_adjust in range(-1,2):
			if is_y_boundary(y+y_adjust, schematic):
				continue
			if schematic[y+y_adjust][x+x_adjust].isdigit():
				process_schematic_part(x+x_adjust,y+y_adjust,schematic)

def part_one(schematic):
	x = 0
	y = 0
	count = 0
	for line in schematic:
		for char in line:
			if is_symbol(char):
				adjacent_numbers(x,y,schematic)
			x += 1
		y += 1
		x = 0
	print('Solution for Day 3, Part 1:' + str(sum(part.value for part in schematic_parts)))