
entries = {}
db = {}

def safeFloat(a):
	if len(a)==0: return 0
	return float(a)

with open('food2.csv','rt') as file:
	for line in file:
		line = line.strip()
		p = line.split('\t')
		item = p[2].strip()
		itemid = '{}_{}_{}'.format(p[0],p[1],p[2].strip())
		if itemid not in entries:
			entries[itemid] = {'type': p[0], 'group':p[1], 'item':item,
				's3':safeFloat(p[3]),
				's4':safeFloat(p[4]),
				's5':safeFloat(p[5])}
		else:
			entry = entries[itemid]
			entry['s4'] = entry['s4'] + safeFloat(p[4])
			entry['s5'] = entry['s5'] + safeFloat(p[5])
			entry['s3'] = entry['s3'] + safeFloat(p[3])

for (linekey,line) in entries.items():
	print(line)
	if line['type'] not in db:
		db[line['type']] = {}
	section = db[line['type']]
	if line['group'] not in section:
		section[line['group']] = {}
	group = section[line['group']]
	score = int((line['s4'] + line['s3'])*6/200)
	if score not in group:
		group[score] = []
	item = line['item']
	if item not in group[score]:
		group[score].append(item)

def ver1():
	with open('p.html','wt') as ofile:
		ofile.write('<html><head></head>')
		ofile.write('<style>')
		ofile.write('td { vertical-align: top; border: 1px solid black;}')
		ofile.write('table { border:1px solid black; }')
		ofile.write('</style>')
		ofile.write('<body>')
		for k,v in db.items():
			ofile.write('<h1>{}</h1>\n'.format(k))
			ofile.write('<table>\n')
			ofile.write('<tr><td>Group</td>')
			for sc in range(6,-7,-1):
				ofile.write('<td style=\'font-size:200%;\'>' + str(sc) + "</td>")
			ofile.write('</tr>\n')
			for k1,v1 in v.items():
				ofile.write('<tr><td>')
				ofile.write(k1)
				ofile.write('</td>\n')
				for sc in range(6,-7,-1):
					ofile.write('<td>')
					if sc in v1:
						for a in v1[sc]:
							ofile.write('<p>' + a + '</p>')
					ofile.write('</td>\n')
				ofile.write('</tr>')
			ofile.write('</table>')
		ofile.write('</body></html>')


with open('p.html','wt') as ofile:
	ofile.write('<html><head></head>')
	ofile.write('<style>')
	ofile.write('td { vertical-align: top; border: 1px solid black;}')
	ofile.write('table { border:1px solid black; }')
	ofile.write('</style>')
	ofile.write('<body>')
	for k,v in db.items():
		ofile.write('<h1>{}</h1>\n'.format(k))
		for k1,v1 in v.items():
			ofile.write('<h2>')
			ofile.write(k1)
			ofile.write('</h2>\n')
			for sc in range(6,-7,-1):
				if sc in v1:
					ofile.write('<p>')
					ofile.write('<b>{}:</b> '.format(sc))
					for a in v1[sc]:
						ofile.write(a + ', ')
					ofile.write('</p>\n')
	ofile.write('</body></html>')
