import check50
import csv
import os

# Function to get the username
def get_username():
    return os.getenv("USER")  # This will get the username from the environment variables

# Function to write results to a CSV file
def write_results(username, check_name, marks):
    file_exists = os.path.isfile("results.csv")
    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Check", "Marks"])  # Write header if file does not exist
        writer.writerow([username, check_name, marks])

@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")
    username = get_username()
    write_results(username, "exists", 5)  # Assuming 5 marks for this check

@check50.check(exists)
def prints_hello():
    """prints "Hello, world!" """
    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n", regex=True).exit(0)
    username = get_username()
    write_results(username, "prints_hello", 10)  # Assuming 10 marks for this check