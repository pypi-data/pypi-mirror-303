
import os

def replace_with_stars(file_path, backup=True):
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    non_space_count = sum(1 for char in content if not char.isspace())

    replacement_content = '*' * non_space_count

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(replacement_content)

    print(f"Replaced content with {non_space_count} stars in '{file_path}'.")


file_path = input("Enter the file path: ")
replace_with_stars(file_path)