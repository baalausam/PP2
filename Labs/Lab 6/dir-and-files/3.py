import os

def check_path(path):
    """Checks if a given path exists and extracts filename and directory."""
    
    if os.path.exists(path):  
        print(f" The path exists: {path}")
        
        
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f" Directory: {directory}")
        print(f" Filename: {filename}")
    
    else:
        print(f" The path does not exist: {path}")

path_to_check = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files\test.txt"
check_path(path_to_check)