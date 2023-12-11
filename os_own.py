import os


def search_files(directory, search_text):
    
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
           
            except Exception as e:
                print(f"error reading file {file_path}: {e}")


if __name__ == "__main__":
    directory = "c:\ioT\Data_structure"
    search_text_input= input('write text: ')


    search_files(directory,search_text_input)





    

