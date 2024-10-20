def str_to_list(sep, s):
    return s.split(sep)
def multi_str_to_list(sep, *args):
    ls = []
    for a in args:
        ls.extend(a.split(sep))
    return ls
def multi_str_to_multi_list(sep, *args):
	ls = []
	for a in args:
		ls.append(str_to_list(sep, a))
	return ls
