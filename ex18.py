def print_two(*args):
# def is define and use to create our won function
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
    
def print_one(arg1):
    print "arg1: %r" % (arg1)
    
def print_none():
    print "I got nothin'."
    

print_two("Shah","Shoib")
print_two_again("Shah","Shoib")
print_one("First!")
print_none()