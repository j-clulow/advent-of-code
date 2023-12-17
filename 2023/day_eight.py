from ast import literal_eval as make_tuple
from math import lcm

def get_map_nodes(map_info):
	map_nodes = dict()
	for line in map_info:
		if line == map_info[0] or line == map_info[1]:
			continue
		node_key = line.split(' = ')[0]
		node_value_string = line.split(' = ')[1].replace(' ','').replace("(","('").replace(",","','").replace(")","')")
		node_values = make_tuple(node_value_string)
		map_nodes[node_key] = node_values
	return map_nodes

def determine_at_destination(nodes):
	for node in nodes:
		if str(node)[-1] != 'Z':
			return False
	return True

def part_one(map_info):
	directions = map_info[0]
	map_nodes = get_map_nodes(map_info)
	current_node = 'AAA'
	steps = 0
	direction_index = 0
	direction_max = len(directions)-1
	while current_node != 'ZZZ':
		direction = directions[direction_index]
		if direction == 'L':
			current_node = map_nodes[current_node][0]
		elif direction == 'R':
			current_node = map_nodes[current_node][1]
		else:
			raise("Unexpected direction encountered: {0}".format(direction))
		steps += 1
		if direction_index == direction_max:
			direction_index = 0
		else:
			direction_index += 1
	print("Day 8 Part 1 Solution is {0} Steps.".format(steps))

def part_two(map_info):
	directions = map_info[0]
	map_nodes = get_map_nodes(map_info)
	current_nodes = list()
	for node in map_nodes:
		if str(node)[-1] == 'A':
			current_nodes.append(node)
	steps = 0
	direction_index = 0
	direction_max = len(directions)-1
	is_all_destinations = False
	while not is_all_destinations:
		direction = directions[direction_index]
		if direction == 'L':
			for index in range(0,len(current_nodes)):
				current_nodes[index] = map_nodes[current_nodes[index]][0]
		elif direction == 'R':
			for index in range(0,len(current_nodes)):
				current_nodes[index] = map_nodes[current_nodes[index]][1]
		else:
			raise("Unexpected direction encountered: {0}".format(direction))
		steps += 1
		if direction_index == direction_max:
			direction_index = 0
		else:
			direction_index += 1
		is_all_destinations = determine_at_destination(current_nodes)
	print("Day 8 Part 2 Solution is {0} Steps".format(steps))

def part_two_lazy(map_info):
	directions = map_info[0]
	map_nodes = get_map_nodes(map_info)
	current_nodes = list()
	for node in map_nodes:
		if str(node)[-1] == 'A':
			current_nodes.append(node)
	step_list = list()
	for node in current_nodes:
		current_node = node
		steps = 0
		direction_index = 0
		direction_max = len(directions)-1
		while str(current_node)[-1] != 'Z':
			direction = directions[direction_index]
			if direction == 'L':
				current_node= map_nodes[current_node][0]
			elif direction == 'R':
				current_node= map_nodes[current_node][1]
			else:
				raise("Unexpected direction encountered: {0}".format(direction))
			steps += 1
			if direction_index == direction_max:
				direction_index = 0
			else:
				direction_index += 1
		step_list.append(steps)
	total_steps = lcm(*step_list)
	print("Day 8 Part 2 Solution is {0} Steps".format(total_steps))