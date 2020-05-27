
entries = {}
db = {}

def safeFloat(a):
	if len(a)==0: return 0
	return float(a)

with open('food.csv','rt') as file:
	for line in file:
		line = line.strip()
		p = line.split('\t')
		item = p[3].strip()
		if len(p[4].strip())>0:
			item += ' ({})'.format(p[4].strip())
		itemid = '{}_{}_{}_{}'.format(p[0],p[1],p[3].strip(),p[4].strip())
		p[3] = item
		p[5] = safeFloat(p[5])
		p[6] = safeFloat(p[6])
		p[7] = safeFloat(p[7])
		if itemid not in entries:
			entries[itemid] = p
		else:
			entry = entries[itemid]
			entry[5] = entry[5] + p[5]
			entry[6] = entry[6] + p[6]
			entry[7] = entry[7] + p[7]

with open('food2.csv','wt') as outf:
	for (linekey,line) in entries.items():
		outf.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(line[0],line[1],line[3],line[5],line[6],line[7]))
