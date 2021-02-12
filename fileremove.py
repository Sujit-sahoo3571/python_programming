import os 

# romove a file using os.remove 

# os.remove('sample.txt')

# another way

if os.path.exists('sample.txt'):
    os.remove('sample.txt')
    print('file deleted successfully! ')
else :
    print('file does not exists ')
