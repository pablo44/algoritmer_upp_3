import os


def search_files(directory, search_text):
    directory = 'c:\ioT\Data_structure'
    
    search_text = input("write your text here: ")
       #we use os walk() function to search the root directory and its files

    for root, dirs, files in os.walk(directory):
        for name in files:
               #this returns tuple of the directories and files and creates a full path of files
            file_path = os.path.join(root, name)
            try:
#we check the files from tuples, reading 'r' the files sotred there
                with open(file_path, 'r') as file:
                        data_path = file.read()

                   #checking if the serarched text is in the results

                        if search_text in data_path:
                            print('yes we hav this')
# now we inform that this file is not readable
            except Exception as e:
                print(f"error reading file {file_path}: {e}")




    

if __name__ == "__main__":
    search_files(directory='c:\ioT\Data_structure',search_text= None)