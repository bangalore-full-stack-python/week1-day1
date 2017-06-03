string = "aabbccddeded"

def my_func(word):
    new_word = " "
    index = 0
    for i in word:
        if i != new_word[index]:
            new_word += i
            index += 1
    print(new_word.strip())

my_func(string)