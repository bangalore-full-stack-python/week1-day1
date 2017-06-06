data = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
data.sort()
# print(data)

def calculate(data):
    # Median
    if (len(data)%2 > 0):
        print (int(int(data[int(len(data)/2)])))
    elif (len(data)%2 == 0):
        print (int(int(data[int(len(data)/2)] + data[int(len(data)/2)-1]) /2))
    
    # Average
    print (int(sum(data)/len(data)))
    
    # Mode
    mcount = 0 
    itm = 0 
    for i in data: 
        if data.count(i)>mcount: 
            mcount = data.count(i) 
            itm = i 
    print (itm)

calculate(data)
