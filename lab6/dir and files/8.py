#write a Python program to delete 
#file by specified path. Before deleting 
#check for access and whether a given path exists or not.
import os
def remove_file(path):
    if(os.access(path,os.F_OK)):
        print(path+' - path exists!')
        os.remove(os.path.basename(path))
        print('the file is removed!')
    else:
        print(path+' - path doesnt exist:^(')
remove_file('C:/Users/ozat1/OneDrive/Рабочий стол/pp2 labs/lab6/dir and files/willbedeleted.py')
remove_file('C:/Users/ozat1/OneDrive/Рабочий стол/pp2 labs/lab6/dir and files/imaginaryfile.txt')
