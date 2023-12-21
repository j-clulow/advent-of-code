def calculate_sequence_pattern(base_sequence):
	sequence_scale = list()
	sequence_scale.append(list(base_sequence))
	is_non_sequence = not (base_sequence is not None and len(base_sequence) > 1)
	while not is_non_sequence:
		current_sequence = sequence_scale[-1]
		new_sequence = list()
		for index in range(0,len(current_sequence)):
			if index == 0:
				continue
			else:
				new_sequence.append(current_sequence[index] - current_sequence[index-1])
		sequence_scale.append(new_sequence)
		is_non_sequence = new_sequence.count(0) == len(new_sequence)
	return sequence_scale

def extrapolate_next_sequence_values(sequences):
	if len(sequences) <= 1:
		return False
	for index in range(len(sequences)-2,-1):
		sequences[index].append(sequences[index][-1] + sequences[index+1][-1])
	return True


	