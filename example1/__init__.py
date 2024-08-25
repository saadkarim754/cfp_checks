import check50  # Import the check50 module

# Global variable to keep track of total marks
total_marks = 0

@check50.check()  # Tag the function below as a check50 check
def exists():
    """hello.py exists (2 marks)"""
    # This check verifies that the file hello.py exists in the student's submission
    global total_marks
    check50.exists("hello.py")
    total_marks += 2  # Award 2 marks for this check

@check50.check(exists)  # Only run this check if the exists check has passed
def prints_hello():
    """prints "Hello, world!" (3 marks)"""
    # This check runs hello.py and verifies that it prints "Hello, world!"
    global total_marks
    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True).exit(0)
    total_marks += 3  # Award 3 marks for this check

def display_total_marks():
    """Displays total marks awarded"""
    print(f"Total Marks Awarded: {total_marks}/5")

# Automatically display the total marks after the checks are run
if __name__ == "__main__":
    display_total_marks()
