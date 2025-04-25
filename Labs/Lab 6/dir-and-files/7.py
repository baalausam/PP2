def copy_file(source_path, destination_path):
    """Copies the contents of one file to another."""
    try:
        with open(source_path, 'r', encoding='utf-8') as src_file:
            content = src_file.read()
        
        with open(destination_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)

        print(f" File copied from:\n{source_path}\nto:\n{destination_path}")
    
    except FileNotFoundError:
        print(" Source file not found.")
    except Exception as e:
        print(f" An error occurred: {e}")


source = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files\test.txt"
destination = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files\copy.txt"

copy_file(source, destination)