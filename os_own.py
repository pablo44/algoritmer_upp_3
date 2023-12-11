import os


def search_files(directory, search_text):
    #path = 'c:\ioT\Data_structure'
    
    #search_text = input("write your text here: ")
       #we use os walk() function to search the root directory and its files
        obj = os.scandir(directory)
    
        for dt in obj:
            file_path = os.path.join(directory, dt.name)

            try:
                if dt.is_file():
        
                    with open(file_path, 'rb') as file:
                        data_path = file.read()

                        if search_text in data_path:

                            print('yes we hav this')

                elif dt.is_dir():
                
                    search_files(file_path, search_text)
                #print(search_text)
            #else:
                #if search_text in data_path:
                           # print('yes we hav this')
                #here we search recursivly directory for files 
                #return search_files(directory, (obj[dt:-1]))
            except Exception as e:
                print(f"error reading file {file_path}: {e}")


if __name__ == "__main__":
    directory = "c:\ioT\Data_structure"
    search_text_input= input('write text: ')


    search_files(directory,search_text_input)


    """for root, dirs, files in os.walk(directory):
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
# here we use recursion to check subdirectories  from the tuples we searched firs, we create a list with dirs to avoid looping in loop
        #for subdirections in list(dirs):
             #search_files(os.path.join(root, subdirections), search_text=None)
"""



    

