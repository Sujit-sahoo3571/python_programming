# file not found handle with try and except 

def FileRead(FileName):
    try:
            
        with open (FileName,'r') as f:
            print(f.read())
    except FileNotFoundError :
        print(f'File {FileName} Not Found ')    

FileRead('F:\\vscode_python\\sem_III_project\\oops\\advancePython\\1.txt')
FileRead('F:\\vscode_python\\sem_III_project\\oops\\advancePython\\2.txt')
FileRead('F:\\vscode_python\\sem_III_project\\oops\\advancePython\\3.txt')