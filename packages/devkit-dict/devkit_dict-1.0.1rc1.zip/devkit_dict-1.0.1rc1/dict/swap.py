def swap(d, a, b):
	d[a], a[b] = d[b], d[a]
	return d
def swap(d, td):
	for k, v in td.items():
		swap(d, k, v)
	return d
