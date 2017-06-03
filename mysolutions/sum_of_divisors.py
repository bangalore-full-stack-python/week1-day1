result = []
div = []

def divisors(number):
    n = 1
    while(n<number):
        if(number%n==0):
            div.append(n)
        else:
            pass
        n += 1
    div.append(number)
    result.append(div)

    sum_div = sum(div)
    result.append(sum_div)
    
    count = len(div)
    result.append(count)

    print (result)

divisors(60)