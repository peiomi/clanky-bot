from functions.write_file import write_file

def run_write_tests():
    test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(test1)
    print(test2)
    print(test3)

run_write_tests()