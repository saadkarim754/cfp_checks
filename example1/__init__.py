import check50  # Import the check50 module
marks = 0
@check50.check()  # Tag the function below as a check50 check
def exists():
    """hello.py exists"""
    marks = marks + 1
    # This check verifies that the file hello.py exists in the student's submission
    check50.exists("hello.py")

@check50.check(exists)  # Only run this check if the exists check has passed
def prints_hello():
    """prints "Hello, world!" """
    marks = marks + 5
    # This check runs hello.py and verifies that it prints "Hello, world!" (case-insensitive, with an optional exclamation mark) and exits with status 0.
    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True).exit(0)

def print_marks():
    print(f"total marks =  {marks}")
