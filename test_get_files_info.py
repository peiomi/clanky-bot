from functions.get_files_info import get_files_info

def run_directory_tests():
    working_dir = "calculator"

    tests = [
        ("current", get_files_info(working_dir, ".")),
        ("'/bin'", get_files_info(working_dir, "/bin")),
        ("'../'", get_files_info(working_dir, "../")),
        ("'pkg'", get_files_info(working_dir, "pkg"))
    ]

    for target_dir, result in tests:
        print(f"Result for {target_dir} directory:")
        print(result)

run_directory_tests()