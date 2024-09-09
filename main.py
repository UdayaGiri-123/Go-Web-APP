import os 

def print_files_in_folder(folder):
        try:
            files = os.listdir(folder)
            return files, None
        except FileNotFoundError:
            return None, "File not found error - " + folder 
        except PermissionError:
            return None, "Insuffiecient permission" + folder 

def main():
    folder_paths = input("Please provide the input folders with space").split()

    for folder in folder_paths:
       files,Errormsg =  print_files_in_folder(folder)
       if files:
            print(f"Files in {folder}:")
            for file in files:
                 print(file)
       else:
            print(f"Files in {folder}:{Errormsg}")


if __name__=="__main__":
    main()