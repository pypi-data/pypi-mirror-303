def count_in_list(obj: list, element) -> int:
	rep = 0
	for x in obj:
		if x == element:
			rep += 1
	return rep
