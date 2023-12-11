def calculate_boundary(time, distance):
	min_hold = 0
	for step in range(0,time+1):
		if step*(time-step) > distance:
			min_hold = step
			break
	return (min_hold, time-min_hold)

def calculated_margin(earliest_release,latest_release):
	return latest_release-earliest_release+1

def part_one(records):
	times = records[0].split()
	times.pop(0)
	distances = records[1].split()
	distances.pop(0)
	record_value = 1
	if len(times) == len(distances):
		index = 0
		for time in times:
			boundaries = calculate_boundary(int(time),int(distances[index]))
			margin = calculated_margin(boundaries[0], boundaries[1])
			if margin > 0:
				record_value = record_value * margin
			index += 1
		print("Day 6 Part 1 Solution is {0}".format(record_value))
	else:
		print("Input was incorrect.")

def part_two(records):
	time = records[0].replace(' ','').split(':')[1]
	distance = records[1].replace(' ','').split(':')[1]
	boundaries = calculate_boundary(int(time),int(distance))
	margin = calculated_margin(boundaries[0],boundaries[1])
	print("Day 6 Part 2 Solution is {0}".format(margin))