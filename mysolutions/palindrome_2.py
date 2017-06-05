def is_palindrome(string):
    string1 = string.split()
    new_string = " "
    new_string.join(string1)

    for i in new_string:
        if (type(i) != chr or type(i) != int):
            del i
            if (new_string == new_string[::-1]):
                print ("True")
            else:
                print ("False")

is_palindrome("A Toyota's a Toyota")