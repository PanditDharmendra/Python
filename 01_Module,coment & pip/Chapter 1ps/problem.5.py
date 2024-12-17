import os

def list_directory_contents(path='.'):
    try:
       # list all file and directy in the given path
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example use with a specified path

path_to_list = '/'        #list your directly path that you want to  run.
list_directory_contents(path_to_list)

