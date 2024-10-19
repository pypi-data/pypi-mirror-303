def write(ls, sep = " ", end = "\n"):
	for i in range(len(ls) - 1):
		print(ls[i], end = sep)
	if len(ls):
		print(ls[len(ls) - 1], end = end)
def write_multi_list(ls, sep = " ", end = "\n"):
	for l in ls:
		write(l, sep, end)
