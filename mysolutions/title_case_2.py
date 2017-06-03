def titlecase(string, exceptions):
    result = ""
    string = string.split()
    for i in string:
        if (i not in exceptions):
            result = result + " " + i.title()
        else:
            result = result + " " + i.lower()
    print (result)

string = "optimus prime and the autobots assembled to fight the decepticons"
exceptions = ['the', 'and', 'decepticons', 'to']

titlecase(string, exceptions)