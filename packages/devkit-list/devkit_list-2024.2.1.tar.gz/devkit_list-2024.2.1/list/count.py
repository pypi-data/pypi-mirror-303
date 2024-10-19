def elemcount(ls):
    vis = []
    for l in ls:
        if not l in vis:
            vis.append(l)
    return {v: ls.count(v) for v in vis}
def elemcount(ls, tls):
	return {t: ls.count(t) for t in tls}
