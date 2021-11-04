from sys import argv

script, filename = argv

# Announce the action we'll do
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# ask for the filename
input("?")
# opens the file
print("Opening the file...")
target = open(filename, 'w')
# erase the file
print("Truncate the file. Goodbye!")
target.truncate()
# ask for the text to be written inside the file
print("Now I'm going to ask you for three lines.")

# user input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Announce what will be done to the file
print("I'm going to write these to the file.")

# take the user input and store it to the file
# return to the line before writing a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# save & close the file

print("And finally, we close it.")
target.close()

