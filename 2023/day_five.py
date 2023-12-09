import re

class SeedMatching:
	seed = -1
	soil = -1
	fertilizer = -1
	water = -1
	light = -1
	temperature = -1
	humidity = -1
	location = -1

	def __init__(self, seed):
		self.seed = seed
	def __repr__(self):
		return "[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}]\n".format(self.seed, self.soil, self.fertilizer, self.water, self.light, self.temperature, self.humidity, self.location)
	def __str__(self):
		return "[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}]\n".format(self.seed, self.soil, self.fertilizer, self.water, self.light, self.temperature, self.humidity, self.location)

def get_map(map_definition):
	map_links = dict()
	map_source = int(map_definition[0])
	map_dest = int(map_definition[1])
	length = int(map_definition[2])
	for index in range(0,length):
		map_links[map_source+index] = map_dest+index
	return map_links

def source_to_dest(map_definitions,source_entries):
	source_destination_links = dict()
	for definition in map_definitions:
		links = get_map(definition)
		for entry in list(source_entries):
			if links.get(entry) != None:
				source_destination_links[entry] = links[entry]
				source_entries.remove(entry)
	for entry in source_entries:
		source_destination_links[entry] = entry
	return source_destination_links

def soil_requirements(seed_infos,seed_soil_map):
	seeds = [seed_info.seed for seed_info in seed_infos]
	links = source_to_dest(seed_soil_map, seeds)
	for seed_info in seed_infos:
		seed_info.soil = links[seed_info.seed]

def fertilizer_requirements(seed_infos, soil_fertilizer_map):
	soils = [seed_info.soil for seed_info in seed_infos]
	links = source_to_dest(soil_fertilizer_map, soils)
	for seed_info in seed_infos:
		seed_info.fertilizer = links[seed_info.soil]

def water_requirements(seed_infos, fertilizer_water_map):
	fertilizers = [seed_info.fertilizer for seed_info in seed_infos]
	links = source_to_dest(fertilizer_water_map, fertilizers)
	for seed_info in seed_infos:
		seed_info.water = links[seed_info.fertilizer]
		
			

def calculate_seed_requirements(seed,mappings):
	seed_information = SeedMatching(seed)
	seed_information.soil = next((entry[1] for entry in mappings[0] if entry[0] == seed_information.seed),seed_information.seed)
	seed_information.fertilizer = next((entry[1] for entry in mappings[1] if entry[0] == seed_information.soil), seed_information.soil)
	seed_information.water = next((entry[1] for entry in mappings[2] if entry[0] == seed_information.fertilizer), seed_information.fertilizer)
	seed_information.light = next((entry[1] for entry in mappings[3] if entry[0] == seed_information.water), seed_information.water)
	seed_information.temperature = next((entry[1] for entry in mappings[4] if entry[0] == seed_information.light), seed_information.light)
	seed_information.humidity = next((entry[1] for entry in mappings[5] if entry[0] == seed_information.temperature), seed_information.temperature)
	seed_information.location = next((entry[1] for entry in mappings[6] if entry[0] == seed_information.humidity), seed_information.humidity)
	return seed_information

def part_one(almanac):
	seeds = almanac[0].split(': ')[1].split(' ')
	section = ''
	sections = [[],[],[],[],[],[],[]]
	for line in almanac:
		if line == almanac[0] or line == almanac[1]:
			continue
		if line[0].isdigit():
			match section:
				case 'seed-to-soil map:':
					sections[0].append(line.split(' '))
				case 'soil-to-fertilizer map:':
					sections[1].append(line.split(' '))
				case 'fertilizer-to-water map:':
					sections[2].append(line.split(' '))
				case 'water-to-light map:':
					sections[3].append(line.split(' '))
				case 'light-to-temperature map:':
					sections[4].append(line.split(' '))
				case 'temperature-to-humidity map:':
					sections[5].append(line.split(' '))
				case 'humidity-to-location map:':
					sections[6].append(line.split(' '))
				case _:
					continue
		elif line[-4:] == 'map:':
			section = line
		else:
			section = ''
	seed_information = []
	for seed in seeds:
		seed_information.append(calculate_seed_requirements(seed, mappings))
	print(seed_information)
	min_loc = -1
	for seed_info in seed_information:
		if min_loc == -1:
			min_loc = seed_info.location
		else:
			min_loc = min(min_loc, seed_info.location)
	print("Day 5, Part 1 Solution: " + str(min_loc))
	