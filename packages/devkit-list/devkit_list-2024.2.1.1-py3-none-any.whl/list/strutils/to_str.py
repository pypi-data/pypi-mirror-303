def list_to_str(ls, sep):
	return sep.join(ls)
def multi_list_to_str(ls, sep):
	s = ""
	for l in ls:
		s += list_to_str(l, sep) + sep
	if len(s):
		s = s[:len(s) - len(sep)]
	return s
