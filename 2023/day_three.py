class SchematicPart:
	x = -1
	y = -1
	length = 0
	value = 0
	gear_location = ''

	def __init__(self, x, y, len, val, loc):
		self.x = x
		self.y = y
		self.length = len
		self.value = val
		self.gear_location = loc

schematic_parts = []

def is_symbol(character):
	return not character.isalnum() and character != '.'

def is_x_boundary(x,schematic):
	return x >= len(schematic[0]) or x < 0

def is_y_boundary(y, schematic):
	return y >= len(schematic) or y < 0

def part_already_counted(x,y):
	return any(part.x == x and part.y == y for part in schematic_parts)

def process_schematic_part(x,y,schematic,sym_x,sym_y,is_gear):
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
	if is_gear:
		schematic_parts.append(SchematicPart(start_x,y,temp_x-start_x,int(number_string),str(sym_x) + ',' + str(sym_y)))
	else:
		schematic_parts.append(SchematicPart(start_x,y,temp_x-start_x,int(number_string),''))
	

def adjacent_numbers(x,y,schematic):
	for x_adjust in range(-1,2):
		if is_x_boundary(x+x_adjust, schematic):
			continue
		for y_adjust in range(-1,2):
			if is_y_boundary(y+y_adjust, schematic):
				continue
			if schematic[y+y_adjust][x+x_adjust].isdigit():
				process_schematic_part(x+x_adjust,y+y_adjust,schematic,x,y,schematic[y][x] == '*')

def part_one(schematic):
	x = 0
	y = 0
	for line in schematic:
		for char in line:
			if is_symbol(char):
				adjacent_numbers(x,y,schematic)
			x += 1
		y += 1
		x = 0
	print('Solution for Day 3, Part 1:' + str(sum(part.value for part in schematic_parts)))

def part_two(schematic):
	x = 0
	y = 0
	for line in schematic:
		for char in line:
			if is_symbol(char):
				adjacent_numbers(x,y,schematic)
			x += 1
		y += 1
		x = 0
	valued_gears = [part.gear_location for part in schematic_parts]
	while valued_gears.count(''):
		valued_gears.remove('')
	gears_to_remove = set()
	for gear_location in valued_gears:
		if valued_gears.count(gear_location) != 2:
			gears_to_remove.add(gear_location)
	for entry in gears_to_remove:
		while valued_gears.count(entry):
			valued_gears.remove(entry)
	gear_ratio_total = 0
	distinct_gears = list(set(valued_gears))
	for gear_loc in distinct_gears:
		parts_adjacent = [part.value for part in schematic_parts if part.gear_location == gear_loc]
		gear_ratio = 1
		for part_value in parts_adjacent:
			gear_ratio = gear_ratio * part_value
		gear_ratio_total += gear_ratio
	print('Solution for Day 3, Part 1:' + str(gear_ratio_total))