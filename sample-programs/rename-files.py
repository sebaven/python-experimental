import os

def rename_files():
    # 1. we get the filenames
    path = r"/Users/sebastien/Documents/workspace/python-programs/samples/prank"
    file_names = os.listdir(path)
    print(file_names)
    
    #2. we loop through the files and rename them
    for file_name in file_names:
        if not file_name.startswith('.'):
            print("current file name: " + file_name)
            new_file_name = file_name.translate(None,"0123456789")
            os.chdir(path)
            print("new file name: " + new_file_name)
            os.rename(file_name, new_file_name)

rename_files()