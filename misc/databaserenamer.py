import re


def remove_strings_and_standalone_n_from_file(input_file_path, output_file_path, strings_to_remove):
    """
    Remove specified strings and standalone occurrences of the character 'N' from a file.

    Parameters:
    input_file_path (str): Path to the input file.
    output_file_path (str): Path to the output file.
    strings_to_remove (list): List of strings to be removed from the file.
    """
    try:
        # Read the content of the file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the specified strings
        for string in strings_to_remove:
            content = content.replace(string, '')

        # Remove standalone 'N' characters
        modified_content = re.sub(r'\bN\b', '', content)

        # Write the modified content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f'Specified strings and standalone character "N" removed and output written to {output_file_path}')

    except FileNotFoundError:
        print(f"The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
input_file = 'input.txt'
output_file = 'output.txt'
strings_to_remove = ['INSERT [dbo].[PLANTPOST] ([UNIQUE], [OFFCODE], [SUBOFFCODE], [SEQUENCE], [STATUS], [POSTNO], [keys], [functions]) VALUES ']

remove_strings_and_standalone_n_from_file(input_file, output_file, strings_to_remove)
