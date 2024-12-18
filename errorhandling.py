# File Read & Write Challenge

def modify_file_content(input_file, output_file):
    """
    Reads content from input_file, modifies it, and writes it to output_file.

    :param input_file: Path to the file to be read.
    :param output_file: Path to the file to write the modified content.
    """
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
            # Modify content: Example - convert to uppercase
            modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

# Error Handling Lab
def handle_user_input():
    """
    Asks the user for a filename and handles errors if the file doesn’t exist or can’t be read.
    """
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

# Example Usage
if __name__ == "__main__":
    # Challenge 1: Modify file content and write to a new file
    modify_file_content("input.txt", "output.txt")

    # Challenge 2: Handle user input and errors
    handle_user_input()
