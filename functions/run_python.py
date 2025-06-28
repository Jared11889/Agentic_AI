import subprocess
from functions.file_handlers import *

def run_python_file(working_directory, file_path):

    abs_working_directory, abs_file_path = get_absolute_locations(working_directory, file_path)

    try:
        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        elif abs_file_path[-3:].lower() != ".py":
            return f'Error: "{file_path}" is not a Python file.'
    except Exception as error:
        print(f"Error: {error}")

        CompletedProcess = None
    try:
        CompletedProcess = subprocess.run(abs_file_path, timeout=30, cwd = abs_working_directory, shell=True)
    except Exception as error:
        return f"Error: executing Python file: {error}"

    result = f"STDOUT: {CompletedProcess.stdout}\n"
    result += f"STDERR: {CompletedProcess.stderr}\n"
    if CompletedProcess.returncode != 0: result += f"Process exited with code {CompletedProcess.returncode}"

    return result