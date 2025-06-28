# from functions.file_handlers import *
from functions.run_python import *

#####Used to test get_files_info#####
# test_cases = (
#     ("calculator", "."),
#     ("calculator", "pkg"),
#     ("calculator", "/bin"),
#     ("calculator", "../")
# )

# def run_tests(test_cases):
#     for case in test_cases:
#         print(f"Input: {case}")
#         print(get_files_info(*case))

# run_tests(test_cases)

#####Used to test get_file_content#####
# content_cases = (
    # ("calculator", "lorem.txt"),
    # ("calculator", "main.py"),
    # ("calculator", "pkg/calculator.py"),
    # ("calculator", "/bin/cat")
# )

# def test_file_content(cases):
#     for case in cases:
#         print(f"Input: {case}")
#         print(get_file_content(*case))

# test_file_content(content_cases)


#####Used to test file_write#####
# write_cases = (
#     ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
#     ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
#     ("calculator", "/tmp/temp.txt", "this should not be allowed")
# )

# def test_file_write(cases):
#     for case in cases:
#         print(f"Input: {case}")
#         print(write_file(*case))

# test_file_write(write_cases)


run_cases = (
    ("calculator", "main.py"),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py")
)

def test_run_python(cases):
    for case in cases:
        print(f"Input: {case}")
        print(run_python_file(*case))

test_run_python(run_cases)