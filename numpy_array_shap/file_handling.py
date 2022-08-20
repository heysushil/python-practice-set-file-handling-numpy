from glob import glob
from msilib import Directory
from pathlib import Path
import sys
import os

# os.rmdir('data_file.txt');exit()
# print(os.chdir('data_file.txt'));exit()
# os.mkdir('data_file.txt')

# file_name = input("Create new file under ", dir_name, ' directory: ')
sub_folders = []
for dir, sub_dirs, files in os.walk('../python/'):
    sub_folders.extend(sub_dirs)
print(sub_folders);exit()

def show_dir_options():
    print('''
    Enter provided number to do following action:

    1. Show Directory
    2. Create Directory
    3. Delete directory

    ''')
    int(input('Enter your option: '))

def show_file_options():
    print('''
    Enter provided number to do following action:

    1. Show Directory related files
    2. Create Directory related file
    3. Delete directory related file

    ''')
    return int(input('Enter your option: '))

def dir_show():
    list_of_avaialbel_dir = glob('../python/*/', recursive=True)

def dir_create(dir_name):
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
        print(dir_name, ' directory is created successfully.\nKnow create file in ', dir_name, ': ')
        show_file_options()
    else:
        print(dir_name, ' extist try new one')
        show_dir_options()

def dir_delete(dir_name):
    if os.path.exists(dir_name) == True:
        os.rmdir(dir_name)
        print(dir_name, ' deleted successfully.')
    else:
        print(dir_name, ' directory not existis in our database, try another?\n')
        show_dir_options()

# print(type(show_dir_options()))
if show_dir_options() == 1:
    dir_show(show_dir_options())
elif show_dir_options() == 2:
    dir_create(input('Enter new directory name: \n'))
elif show_dir_options() == 3:
    dir_delete(input('Enter directory name: \n'))
else:
    show_dir_options()    

# if os.path.exists(file_name) == False:
#     os.mkdir(file_name)
#     print(file_name, ' file is created successfully.')
# print(os.path.exists(dir_name))