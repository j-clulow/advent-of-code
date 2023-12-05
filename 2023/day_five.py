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

def source_to_dest(maps):
	source_dest_links = []
	for entry in maps:
		source_start = entry[0][0]
		dest_start = entry[0][1]
		length = entry[0][2]
		for index in range(0,length):
			source_dest_links.append((source_start+index,dest_start+index))
	return source_dest_links

def get_maps(almanac_section):
	regex = r"(seed|soil|fertilizer|water|light|temperature|humidity)-to-(soil|fertilizer|water|light|temperature|humidity|location) map:"
	if not re.match(regex,almanac_section[0]):
		return []
	maps = []
	for line in almanac_section:
		if line == almanac_section[0]:
			continue
		maps.append(line.split(' '))
	return source_to_dest(maps)

def seed_to_soil(almanac_section):
	if almanac_section[0] != 'seed-to-soil mail:\n':
		return []
	seed_soil_records = []
	for line in almanac_section:
		if line == almanac_section[0]:
			continue
		seed_soil_records.append(line.split(' '))
	return source_to_dest(seed_soil_records)

def part_one(almanac):
	