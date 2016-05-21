from sys import argv

script, last_name = argv

prompt = ': '

print "Hi %s, I am the %s script." % (last_name, script)

print "I'd like to ask you some questions:"


print "What is your first name %s" % last_name
first_name = raw_input(prompt)
# Will store the input in the first_name varaible


print "What is your middle name %s" % last_name
middle_name = raw_input(prompt)
# Will store the input in the middle_name varaible

print """
Alright, so your full name is %s %s %s
""" % (first_name, middle_name, last_name)

