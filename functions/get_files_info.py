import os

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error: {error}")
    return inner


def get_files_info(working_directory, directory=None):

    if not error_handler(abs_directory.startswith(abs_working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not error_handler(os.path.isdir(abs_directory)):
        return f'Error: "{directory}" is not a directory'
    
    abs_working_directory = error_handler(os.path.abspath(working_directory))
    abs_directory = error_handler(os.path.abspath(directory))
    dir = error_handler(os.listdir(abs_directory))
    result = ""

    for item in dir:
        
        filesize = error_handler(os.path.getsize(os.path.join(abs_directory, item)))
        isdir = error_handler(os.path.isdir(os.path.join(abs_directory, item)))
        result += f"- {item}: file_size={filesize} bytes, is_dir={isdir}\n"

    return result