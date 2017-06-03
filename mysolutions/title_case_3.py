def titlecase(string, exceptions):
	result = ""
	string = string.split()
	for i in string:
		if (i not in exceptions):
			result = result + " " + i.lower()
		else:
			result = result + " " + i.upper()
	print(result)

string = "optimus prime and the autobots assembled to fight the decepticons"
exceptions = ['optimus', 'prime', 'autobots', 'victorious']

titlecase(string, exceptions)