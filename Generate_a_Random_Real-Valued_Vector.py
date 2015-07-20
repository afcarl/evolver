# Implementation of Generate a Random Real-Valued Vector
import random
import math

# constants
V_MIN = 0.0 # minimum desired vector element value
V_MAX = 10.0 # maximum desired vector element value
V_LENGTH = 10 # vector length

# define vector class
class Vector:
    def __init__(self, length):
        # initialized the container for vector
        self.vectorLength = length
        self.vectorContainer = [0] * self.vectorLength
    # assign a new value to a given index element
    def assign(self, newValue, index):
        self.vectorContainer[index] = newValue
    # return the vector string
    def toString(self):
        # create vector string
        vectorString = "<"
        for index in range(self.vectorLength-1):
            vectorString += str(round(self.vectorContainer[index], 3)) + ", "
        vectorString +=\
                str(round(self.vectorContainer[self.vectorLength-1], 3)) + ">"
        return vectorString

# Generate a Random Real-Valued Vector main function
def generate_a_random_real_valued_vector():
    print "Generation of a Random Real-Valued Vector: "
    # generate a new vector
    newRandomVector = Vector(V_LENGTH)
    for index in range(V_LENGTH):
        randomValue = random.uniform(V_MIN, V_MAX)
        newRandomVector.assign(randomValue, index)
    # print the vector
    print newRandomVector.toString()

# execute
generate_a_random_real_valued_vector()
