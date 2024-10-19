def for_each(ls, func, *args, **kwargs):
	return [func(l, *args, **kwargs) for l in ls]
