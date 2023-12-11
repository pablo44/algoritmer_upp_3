import os

#creating func to search text in directory
def search_files(directory, search_text):

#creating en iterator obj of scandir method   
        obj = os.scandir(directory)
#looping through objects that has inbuld atribute  'name'
        for dt in obj:
            file_path = os.path.join(directory, dt.name)
#checking if the result in file path is a file, reading it, and finaly frinting suscesuly found file
            try:
                if dt.is_file():

                    with open(file_path, 'rb') as file:
                        data_path = file.read()

                        if search_text in data_path:
                            print('yes we hav this')
#if object dt is directory we have to again search for files using recursive call of search_files with atributes 'file_path' and 'searchtext'
                elif dt.is_dir():                
                    search_files(file_path, search_text)
        #showing the error when the file is not readible
            except Exception as e:
                print(f"error reading file {file_path}: {e}")


if __name__ == "__main__":
    directory = "c:\ioT\Data_structure"
    search_text_input= input('write text: ')


    search_files(directory,search_text_input)





    

