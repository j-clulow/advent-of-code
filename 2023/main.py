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

def run_four():
	data = read_puzzle_input(".\datafiles\day_four.txt")
	from day_four import part_one
	part_one(data)
	from day_four import part_two
	part_two(data)

def run_five():
	data = read_puzzle_input(".\datafiles\day_five.txt")
	from day_five import part_one
	part_one(data)
	from day_five import part_two
	part_two(data)

def run_six():
	data = read_puzzle_input(".\datafiles\day_six.txt")
	from day_six import part_one
	part_one(data)
	from day_six import part_two
	part_two(data)

def run_seven():
	data = read_puzzle_input(".\datafiles\day_seven.txt")
	from day_seven import part_one
	part_one(data)
	from day_seven import part_two
	part_two(data)

def run_eight():
	data = read_puzzle_input(".\datafiles\day_eight.txt")
	from day_eight import part_one
	part_one(data)
	from day_eight import part_two_lazy
	part_two_lazy(data)

# run_one()
# run_two()
# run_three()
# run_four()
# run_five()
# run_six()
# run_seven()
run_eight()