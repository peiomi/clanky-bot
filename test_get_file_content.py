from functions.get_file_content import get_file_content

def run_path_tests():
    working_directory = "calculator"
    test1 = get_file_content(working_directory, "lorem.txt")
    print(f"lorem.txt length: {len(test1)}")
    print(f"lorem.txt truncated: {'truncated' in test1}")

    test2 = get_file_content(working_directory, "main.py")
    test3 = get_file_content(working_directory, "pkg/calculator.py")
    test4 = get_file_content(working_directory, "/bin/cat")
    test5 = get_file_content(working_directory, "pkg/does_not_exist.py")
    print(test2)
    print(test3)
    print(test4)
    print(test5)

run_path_tests()