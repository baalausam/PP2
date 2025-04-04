def write_list_to_file(file_path, data_list):
    """Writes each item from the list to a text file on a new line."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f" List successfully written to: {file_path}")
    except Exception as e:
        print(f" Error writing to file: {e}")


my_list = ['Apple', 'Banana', 'Cherry', 'Orange']


file_path = r"C:\Users\Admin\Desktop\PP2\Labs\Lab 6\dir-and-files\output.txt"
write_list_to_file(file_path, my_list)