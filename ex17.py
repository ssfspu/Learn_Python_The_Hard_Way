
from sys import argv
# Imports the argument variable which let's us specify information in the command line 
from os.path import exists
# os.path is used because different operating systems specify files paths in different ways.
# "exists" is  a function that returns "TRUE" if the file path is valid i.e. file exists and the 
# user has permissions.

script, from_file, to_file = argv
# name of the script, file from which we copying the text, file to which we copying the text 

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?

in_file = open(from_file)

indata = in_file.read()

print " The input file is %d bytes long" % len(indata)
#len() is function useful in some situation and gets the length of the string

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input()

out_file = open(to_file, 'w')

out_file.write(indata)

print "Alright, all done."

out_file.close()

in_file.close()