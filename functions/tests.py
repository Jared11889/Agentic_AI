from get_files_info import *

test_cases = (
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
)

def run_tests(test_cases):
    for case in test_cases:
        print(f"Input: {case}")
        print(get_files_info(*case))

run_tests(test_cases)