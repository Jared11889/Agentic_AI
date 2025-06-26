import os

def get_file_content(working_directory, file_path, MAX_CHARS=10000):

    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    except Exception as error:
        print(f"Error: {error}")

    try:
        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as error:
        print(f"Error: {error}")

    file_content_string = ""
    try:
        with open(abs_file_path, "r") as file:
            file_content_string = file.read(MAX_CHARS+1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:-1] + f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as error:
        print(f"Error: {error}")

    return file_content_string