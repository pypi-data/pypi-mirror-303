def read(n, s = "", func = lambda s: s):
	return [func(input(s)) for i in range(n)]
def read_split(s = "", spl = " ", func = lambda s: s):
	return [func(i) for i in input(s).split(spl)]
def read_multi_list(m, n, s = "", func = lambda s: s):
	return [read(n, s, func) for i in range(m)]
def read_multi_list_split(m, s = "", spl = " ", func = lambda s: s):
	return [read_split(s, spl, func) for i in range(m)]
