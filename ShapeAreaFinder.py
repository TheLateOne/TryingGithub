def find_shape():
    shape = raw_input("What shape do you want to find the area of [square/triangle/circle/rectangle]? \n >> ")
    return eval(shape)

def square():
    print "IT WORKED"

def triangle():
    lengths_tri = raw_input("What is the height and base of the triangle? \n >> ")
    x = lengths_tri.split()
    z = (float(x[0]) * float(x[1])) / 2
    return z

def circle():
    pass
def rectangle():
    square()

def run():
    s = find_shape()
    print s()

run()