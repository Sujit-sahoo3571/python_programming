import os 

# folderpath name 
folderPath = 'F:\\EVRSYSTEM\\OIDV4_ToolKit\\OID\\Dataset\\train\\Ambulance\\Label'
newlist = []

# write out put into a file

f = open('listforEVR.txt','a')

def listDir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        # print name of file without .txt extension 
        # print(os.path.splitext(filename)[0]  )
       newlist .append(os.path.splitext(filename)[0] ) 
       f.write(os.path.splitext(filename)[0]+'\n')
    print(newlist)    

listDir(folderPath)

f.close()