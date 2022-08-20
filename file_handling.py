from glob import glob
from msilib import Directory
from pathlib import Path
import sys
import os

# os.rmdir('data_file.txt');exit()
# print(os.chdir('data_file.txt'));exit()
# os.mkdir('data_file.txt')

# file_name = input("Create new file under ", dir_name, ' directory: ')
main_directory_name = 'python'

# print(subfolders);exit()
# print(files);exit()

print('''
Enter provided number to do following action:

1. Show Directory
2. Create Directory
3. Delete directory
4. Exit
''')
user_option = int(input('Enter your option: '))

def show_dir_options():
    print('''
    Enter provided number to do following action:

    1. Show Directory
    2. Create Directory
    3. Delete directory
    4. Exit
    ''')
    user_option = int(input('Enter your option: '))
    options_action(user_option)

def options_action(user_option):
    if user_option == 1:
        dir_show()
    elif user_option == 2:
        dir_create(input('Enter new directory name: \n'))
    elif user_option == 3:
        dir_delete(input('Enter directory name: \n'))
    elif user_option == 4:
        print('\nThank you for visit!\n')
        exit()
    else:
        print('\n!!!!!!!!!You enterd wrong input try again between 1 to 4 inputes only: \n')
        show_dir_options()   

def show_file_options_message():
    print('''
    Enter provided number to do following action:

    1. Show Directory related files
    2. Create Directory related file
    3. Delete directory related file
    4. Exit

    ''')
    file_option_input = int(input('Enter your option: '))
    # return file_option_input
    show_file_options(file_option_input)

def show_file_options(user_option):
    if user_option == 1:
        pass # dir_related_files_show()
    elif user_option == 2:
        pass # dir_related_file_create(input('Enter new file name: \n'))
    elif user_option == 3:
        pass # dir_releted_file_delete(input('Enter directory file name name: \n'))
    elif user_option == 4:
        print('\nThank you for visit!\n')
        exit()
    else:
        print('\n!!!!!!!!!You enterd wrong input try again between 1 to 4 inputes only: \n')
        show_file_options_message()   

def dir_show():
    subfolders = [ f.path[10:] for f in os.scandir('../'+main_directory_name+'/') if f.is_dir() ]
    print('\nAvailabel Directory names are: \n')
    for i,s in enumerate(subfolders, start=1):
        print(i,s)
    # print('\n')
    # call option action function and pass show dir option return value to it for choosing option as per user input
    user_option = show_dir_options()
    options_action(user_option)

def dir_create(dir_name):
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
        print(dir_name, ' directory is created successfully.\nKnow create file in ', dir_name, ': ')
        show_file_options_message()
    else:
        print(dir_name, ' extist try new one.\n')
        dir_create(input('Enter new directory name: \n'))

def dir_delete(dir_name):
    if os.path.exists(dir_name) == True:
        os.rmdir(dir_name)
        print(dir_name, ' deleted successfully.\n')
        show_dir_options()
    else:
        print(dir_name, ' directory not existis in our database, try another?\n')
        show_dir_options()

# print(type(show_dir_options()))
if user_option == 1:
    dir_show()
elif user_option == 2:
    dir_create(input('Enter new directory name: \n'))
elif user_option == 3:
    dir_delete(input('Enter directory name: \n'))
elif user_option == 4:
    print('\nThank you for visit!\n')
    # exit()
else:
    print('\n!!!!!!!!!You enterd wrong input try again between 1 to 4 inputes only: ')
    show_dir_options()   

# if os.path.exists(file_name) == False:
#     os.mkdir(file_name)
#     print(file_name, ' file is created successfully.')
# print(os.path.exists(dir_name))