List1 = [10, 20, 30, 40, 50]
Count = len(List1)
for i in range (len(List1)):
    if i == 0:
        temp = List1[0]
    elif i == Count-1:
        List1[0] = List1[i]
        List1[i] = temp

print(List1)


