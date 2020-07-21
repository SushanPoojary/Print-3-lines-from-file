from sys import argv

script, input_file = argv

def print_all(f):
	print(">>>>> print_all:", f) #just to se entry
	print(f.read()) #read
	print("<<<<< print_all:", f, "\n") #check exit

def rewind(f):
	print(f.seek(0)) #seek


def print_line(line_count, f):
	print(line_count, f.readline()) #read single line


current_file = open(input_file)

print("Let's print the whole line: \n")
print_all(current_file)

print("Let's rewind")
rewind(current_file)


print("Let's print 3 lines: ")

current_line = 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)

current_line = current_line + 1
print_line(current_line, current_file)