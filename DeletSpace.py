def remove_spaces_from_file(input_file, output_file):
    try:
        # Read File
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Delete All Spaces
        content_no_spaces = content.replace(" ", "")

        # Write new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content_no_spaces)

        print(f"Spaces '{input_file}' deleted and new file is '{output_file}'.")

    except Exception as e:
        print(f"Error: {e}")


# Use
input_file = 'C:/Users/Cafu/Downloads/file.txt'  # Your file name
output_file = 'C:/Users/Cafu/Downloads/file2.txt'  # Exit file name
remove_spaces_from_file(input_file, output_file)