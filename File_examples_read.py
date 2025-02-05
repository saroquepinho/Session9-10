fp = open("text.txt", "r") # r is by default, so not really needed
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close the file

# same command with contect manager
with open("text.txt", "r") as fp:
    print(fp.read())

# Lets read from the same file, line by line
print("Read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp: # we interate the file, line by line

        print(f"{line_number}:{line}", end="") #ask print not to add a new line
        # print(line.rstrip())
        line_number += 1
# if it adds an extra line next our text, just add print()
print("done printing")
