string = "balloons"
result = []

def my_func(word):
    new_word = " "
    rep = ""
    index = 0
    for i in word:
        if i != new_word[index]:
            new_word += i
            index += 1
        else:
            rep += i
    result.append(new_word.strip())
    result.append(rep)
    print(result)

my_func(string)