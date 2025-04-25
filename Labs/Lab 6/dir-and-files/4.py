def count_lines(file_path):
    """Counts the number of lines in a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            print(f" File: {file_path}")
            print(f" Total lines: {len(lines)}")
    except FileNotFoundError:
        print(f" Error: File not found - {file_path}")
    except Exception as e:
        print(f" An error occurred: {e}")


file_path = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files"
count_lines(file_path)