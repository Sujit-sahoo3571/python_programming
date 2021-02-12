import os 

# folderpath name 
folderPath = 'F:\\EVRSYSTEM\\OIDV4_ToolKit\\OID\\Dataset\\train\\Ambulance\\Label'

def listDir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        # print('fileName '+ filename)
        print(os.path.splitext(filename)[0] )
        # print('Folder Path '+ os.path.abspath(os.path.join(dir,filename)),sep='\n')

    

listDir(folderPath)

    