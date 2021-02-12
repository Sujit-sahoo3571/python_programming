# print using enumerate , list of 3,5,7 element

list1 = [33,55,35,23,64,77,79,0,90]

for idx,num in enumerate(list1):
    if (idx == 2 or idx ==4 or idx == 6):
        print(num, idx )