import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it contains 2 dollars")
elif type == "t2.medium":
    print("it contains 4 dollars")
elif type == "t3.medium":
    print("it contains 8 dollars")
else:
    print("provide valid instance type")
