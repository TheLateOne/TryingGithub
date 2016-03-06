import math

def find_shape():
    shape = raw_input("What shape do you want to find the area of [square/triangle/circle/rectangle]? \n >> ")
    return eval(shape)

def square():
    edge_length = raw_input("What are the lengths of the two sides of the quadrilateral? \n >> ")
    x = edge_length.split()
    return int(x[0]) * int(x[1])

def triangle():
    lengths_tri = raw_input("What is the height and base of the triangle? \n >> ")
    x = lengths_tri.split()
    return (float(x[0]) * float(x[1])) / 2

def circle():
    circle_info = input("What is the radius of the circle? \n >> ")
    return math.pi * circle_info ** 2

def rectangle():
    return square()

def run():
    s = find_shape()
    print s()

run()