from functions.get_files_info import get_files_info

test1 = get_files_info("calculator", ".")
test2 = get_files_info("calculator", "/bin")
test3 = get_files_info("calculator", "../")
test4 = get_files_info("calculator", "main.py")

print(test1)
print(test2)
print(test3)
print(test4)