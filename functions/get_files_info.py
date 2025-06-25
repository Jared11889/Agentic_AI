import os

def get_files_info(working_directory, directory=None):

    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(os.path.join(abs_working_directory, directory))
    except Exception as error:
        print(f"Error: {error}")

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