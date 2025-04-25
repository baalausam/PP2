import string
import os

def generate_text_files(folder_path):
    """Generates 26 text files named A.txt to Z.txt in the specified folder."""
    try:
        os.makedirs(folder_path, exist_ok=True)  

        for letter in string.ascii_uppercase:  
            file_name = f"{letter}.txt"
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"This is file {file_name}")
        
        print(f" 26 files (A.txt to Z.txt) created in: {folder_path}")

    except Exception as e:
        print(f" Error creating files: {e}")


folder = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files\letters"
generate_text_files(folder)