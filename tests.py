from functions.file_handlers import *

#####Used to test get_files_info.py.#####
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

content_cases = (
    ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat")
)

def test_file_content(cases):
    for case in cases:
        print(f"Input: {case}")
        print(get_file_content(*case))

test_file_content(content_cases)