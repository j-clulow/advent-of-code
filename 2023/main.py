##day_imports = ['day_one','day_two']
import pathlib

def read_puzzle_input(filename):
	from pathlib import Path
	path = Path(__file__).parent/filename
	with path.open() as file:
		input_list = file.read().splitlines()
	return input_list

def run_one():
	data = read_puzzle_input(".\datafiles\day_one.txt")
	from day_one import part_one
	part_one(data)
	from day_one import part_two
	part_two(data)

def run_two():
	data = read_puzzle_input(".\datafiles\day_two.txt")
	from day_two import part_one
	part_one(data)
	from day_two import part_two
	part_two(data)

def run_three():
	data = read_puzzle_input(".\datafiles\day_three.txt")
	from day_three import part_one
	part_one(data)
	from day_three import part_two
	part_two(data)

# run_one()
# run_two()
run_three()
