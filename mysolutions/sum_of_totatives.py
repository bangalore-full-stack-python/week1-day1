import fractions

def sum_tot(number):
    i = 0
    result = []
    totatives = []
    while i < number:
        gcd = fractions.gcd(i,number)
        if gcd == 1:
            totatives.append(i)
        i = i + 1
    result.append(totatives)

    add = sum(totatives)
    result.append(add)

    count = len(totatives)
    result.append(count)

    print(result)

sum_tot(30)