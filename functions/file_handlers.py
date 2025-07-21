import os
from config import MAX_CHARS

def get_absolute_locations(working_directory, target):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(os.path.join(abs_working_directory, target))
    except Exception as error:
        print(f"Error: {error}")

    return abs_working_directory, abs_directory

def get_files_info(working_directory, directory=None):

    abs_working_directory, abs_directory = get_absolute_locations(working_directory, directory)

    #valid working directory check
    try:
        if not abs_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'
    except Exception as error:
        print(f"Error: {error}")

    try:
        dir = os.listdir(abs_directory)
    except Exception as error:
        print(f"Error: {error}")

    result = ""
    for item in dir:
        try:
            filesize = os.path.getsize(os.path.join(abs_directory, item))
            isdir = os.path.isdir(os.path.join(abs_directory, item))
            result += f"- {item}: file_size={filesize} bytes, is_dir={isdir}\n"
        except Exception as error:
            print(f"Error: {error}")    
    return result


def get_file_content(working_directory, file_path, MAX_CHARS=MAX_CHARS):

    abs_working_directory, abs_file_path = get_absolute_locations(working_directory, file_path)

    #valid working directory check
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


def write_file(working_directory, file_path, content):

    abs_working_directory, abs_file_path = get_absolute_locations(working_directory, file_path)

    #valid working directory check
    try:
        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    except Exception as error:
        print(f"Error: {error}")

    #make directory if needed
    try:
        if not os.path.isdir(os.path.split(abs_file_path)[0]):
            os.makedirs(os.path.split(abs_file_path)[0],exist_ok=True)
    except Exception as error:
        print(f"Error: {error}")

    #create file
    try:
        with open(abs_file_path, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as error:
        print(f"Error: {error}")
    