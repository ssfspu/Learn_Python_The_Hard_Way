from sys import argv

script, filename = argv

# Need to include the name of the text file  in the command line when you run the python script

# If you are writing or appending then a new file will be created with the name if one 
# does not already exist

print "We're going to erase %r." % filename

print "if you don't want that, hit CTRL-C (^C)."

print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file...."

target = open(filename,'a')

# w = write, r = read, a = append

# r+ = read and write
# w+ = write and read
# r read only is default

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the files."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

target.close()


