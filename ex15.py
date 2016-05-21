from sys import argv

script, filename = argv

txt = open (filename)

# "open" is a command that reads the text file
# as long as you put the name of the file in 
# the command line when you ran the script

print "Here's your file %r:" % filename

print txt.read()

# txt is a variable or object and the . (dot)
# is to add a command, "read" in this case.
# The parentheses () have to be there but in this
# there is not argument to pass

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open (file_again)

print txt_again.read()

txt.close
txt_again.close

# close the files