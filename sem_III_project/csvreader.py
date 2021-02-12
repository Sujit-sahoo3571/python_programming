import numpy as np
import pandas as pd
import os 

folderPath = 'F:\\EVRSYSTEM\\OIDV4_ToolKit\\OID\\Dataset\\train\\Ambulance\\Label'
newlist = []

def listDir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        newlist .append(os.path.splitext(filename)[0] )
    print(newlist)    

listDir(folderPath)


iris = pd.read_csv('F:\\EVRSYSTEM\\OIDV4_ToolKit\\OID\\csv_folder\\train-annotations-bbox.csv')

val = iris.loc[iris['ImageID'].isin(newlist)]

val.to_excel('listforEVR.xlsx', index = False , header = True )