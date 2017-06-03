bio_data = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]

def iter(lst):
	for i in lst:
		if (i == 1 or i == 2):
			print (i)
		elif (i != 1 and i != 2 and type(i) == list):
			for j in i:
				if (type(j) == str or type(j) == int):
					print(j)
				elif (type(j) == list):
						for k in j:
							print (k)

iter(bio_data)