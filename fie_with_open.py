# best way to open a file and close a  file automatically
# and no need to close using f.close()
# can open for read , write , append 

with open('myname.txt') as f:
   text =  f.read()
   print(text)

# with is a function like it need (:) and (indent) and (as)  


with open ('another.txt', 'w') as f:
    f.write('test case 1 ')


with open ('another.txt', 'a') as f:
    f.write('\n i created new file in vs code using\
write mode and now i append this .  ')