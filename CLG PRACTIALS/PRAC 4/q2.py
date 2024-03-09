import os

filename = "q2.txt"

if not os.path.exists(filename):
    file = open(filename, "w")
    print("File opened for writing:", file.name)
else:
    with open(filename, "r") as file:
        print("File already exists and opened for reading:", file.name)
        # Define the pattern you want to search for
        search_pattern = "Line 1:"

        # Read the file line by line
        for line_number, line in enumerate(file, 1):
            if search_pattern in line:
                print(f"Pattern found in line {line_number}: {line.strip()}")
