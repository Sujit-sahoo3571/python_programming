# print the multiplication table 
# print in making different file/folder

for i in range (2 , 21): 
    with open (f'table/mulTable{i}.txt','w') as f :
        for j in range(1,11):
            f.write(f"{i} X {j} = { i * j }")
            if (j != 10):
                f.write('\n')

print('Changes done in table file that\
 you spacify the path here ')