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

def get_map(map_definition,source_values):
	map_links = dict()
	map_dest = int(map_definition[0])
	map_source = int(map_definition[1])
	length = int(map_definition[2])
	max_source = map_source+length
	for source in source_values:
		if int(source) >= int(map_source) and int(source) <= int(max_source):
			map_links[int(source)] = int(map_dest)+(int(source)-int(map_source))
	return map_links

def source_to_dest(map_definitions,source_entries):
	source_destination_links = dict()
	entries = list(source_entries)
	for definition in map_definitions:
		links = get_map(definition, entries)
		for entry in list(entries):
			if links.get(int(entry)) != None:
				source_destination_links[int(entry)] = links[int(entry)]
				entries.remove(int(entry))
	for entry in entries:
		source_destination_links[int(entry)] = int(entry)
	return source_destination_links

def soil_requirements(seed_infos,seed_soil_map):
	seeds = [seed_info.seed for seed_info in seed_infos]
	links = source_to_dest(seed_soil_map, seeds)
	for seed_info in seed_infos:
		seed_info.soil = int(links[int(seed_info.seed)])

def fertilizer_requirements(seed_infos, soil_fertilizer_map):
	soils = [seed_info.soil for seed_info in seed_infos]
	links = source_to_dest(soil_fertilizer_map, soils)
	for seed_info in seed_infos:
		seed_info.fertilizer = int(links[int(seed_info.soil)])

def water_requirements(seed_infos, fertilizer_water_map):
	fertilizers = [seed_info.fertilizer for seed_info in seed_infos]
	links = source_to_dest(fertilizer_water_map, fertilizers)
	for seed_info in seed_infos:
		seed_info.water = int(links[int(seed_info.fertilizer)])
		
def light_requirements(seed_infos, water_light_map):
	waters = [seed_info.water for seed_info in seed_infos]
	links = source_to_dest(water_light_map, waters)
	for seed_info in seed_infos:
		seed_info.light = int(links[int(seed_info.water)])

def temperature_requirements(seed_infos, light_temperature_map):
	lights = [seed_info.light for seed_info in seed_infos]
	links = source_to_dest(light_temperature_map, lights)
	for seed_info in seed_infos:
		seed_info.temperature = int(links[int(seed_info.light)])

def humidity_requirements(seed_infos, temperature_humidity_map):
	temps = [seed_info.temperature for seed_info in seed_infos]
	links = source_to_dest(temperature_humidity_map, temps)
	for seed_info in seed_infos:
		seed_info.humidity = int(links[int(seed_info.temperature)])

def location_requirements(seed_infos, humidity_location_map):
	humidities = [seed_info.humidity for seed_info in seed_infos]
	links = source_to_dest(humidity_location_map, humidities)
	for seed_info in seed_infos:
		seed_info.location = int(links[int(seed_info.humidity)])

def calculate_seed_requirements(seed_infos,mappings):
	soil_requirements(seed_infos,mappings[0])
	fertilizer_requirements(seed_infos,mappings[1])
	water_requirements(seed_infos,mappings[2])
	light_requirements(seed_infos,mappings[3])
	temperature_requirements(seed_infos,mappings[4])
	humidity_requirements(seed_infos,mappings[5])
	location_requirements(seed_infos,mappings[6])

def process_almanac(almanac, sections):
	section = ''
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

def get_minimum_location(seeds, almanac_sections):
	min_location = -1
	seed_information = []
	for seed in seeds:
		seed_information.append(SeedMatching(int(seed)))
	calculate_seed_requirements(seed_information, almanac_sections)
	for seed_info in seed_information:
		if min_location == -1:
			min_location = seed_info.location
		else:
			min_location = min(min_location, seed_info.location)
	return min_location
	

def part_one(almanac):
	seeds = almanac[0].split(': ')[1].split(' ')
	sections = [[],[],[],[],[],[],[]]
	process_almanac(almanac, sections)
	seed_information = []
	for seed in seeds:
		seed_information.append(SeedMatching(int(seed)))
	calculate_seed_requirements(seed_information, sections)
	min_loc = -1
	for seed_info in seed_information:
		if min_loc == -1:
			min_loc = seed_info.location
		else:
			min_loc = min(min_loc, seed_info.location)
	print("Day 5, Part 1 Solution: " + str(min_loc))

def part_two(almanac):
	seed_definitions = almanac[0].split(': ')[1].split(' ')
	count = int(len(seed_definitions)/2)
	print(count)
	message_count = 1
	update_count = 0
	seeds = list()
	sections = [[],[],[],[],[],[],[]]
	process_almanac(almanac, sections)
	min_loc = -1
	for index in range(0,count):
		seed_start = int(seed_definitions[index*2])
		seed_range = int(seed_definitions[index*2+1])
		for seed_increment in range(0,seed_range+1):
			seeds.append(seed_start+seed_increment)
			if len(seeds) >= 10000 or seed_increment == seed_range:
				batch_minimum = int(get_minimum_location(seeds,sections))
				if min_loc == -1:
					min_loc = batch_minimum
				else:
					min_loc = min(batch_minimum, min_loc)
				seeds.clear()
				if update_count < 100:
					update_count += 1
				if update_count == 100:
					print("Finished Batch {0}. Minimum is {1}".format(message_count,min_loc))
					update_count = 0
					message_count += 1
	print("Day 5, Part 2 Solution: " + str(min_loc))