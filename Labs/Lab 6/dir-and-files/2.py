import os

def check_access(path):
    """Checks if the specified path exists and its permissions (read, write, execute)."""
    
    print(f"Checking access for: {path}")
    
    if os.path.exists(path):
        print("Path exists.")
        print("Readable:", os.access(path, os.R_OK))
        print("Writable:", os.access(path, os.W_OK))
        print("Executable:", os.access(path, os.X_OK))
    else:
        print("Path does not exist.")

path_to_check = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files"

check_access(path_to_check)