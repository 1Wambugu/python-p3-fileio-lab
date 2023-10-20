def write_file(file_name, file_content):
    """
    Write the given content to a text file.

    :param file_name: The name of the file (without the extension).
    :param file_content: The content to write to the file.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    """
    Append the given content to an existing text file.

    :param file_name: The name of the file (without the extension).
    :param append_content: The content to append to the file.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "a") as file:
        file.write(append_content)

def read_file(file_name):
    """
    Read the content of a text file.

    :param file_name: The name of the file (without the extension).
    :return: The content of the file as a string.
    """
    file_path = f"{file_name}.txt"
    with open(file_path, "r") as file:
        return file.read()
