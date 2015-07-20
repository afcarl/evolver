# Implementation of Bounded Uniform Convolution
import random
import math

# constants
V_MIN = 0.0 # minimum desired vector element value
V_MAX = 10.0 # maximum desired vector element value
V_LENGTH = 10 # vector length
P_NOISE = 1.0 # probability of adding noise to an element in the vector
R_NOISE = 0.01 # half-range of uniform noise

# define vector class
class Vector:
    # initialize the container for vector
    def __init__(self, length=10):
        self.vectorLength = length
        self.vectorContainer = [0] * self.vectorLength
    # return an element of the vector at given index
    def get(self, index):
        return self.vectorContainer[index]
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

# loop stops when the condition is not met
def loop_condition_is_met(vectorElement, randomNumber):
    return vectorElement + randomNumber < V_MIN and\
            vectorElement + randomNumber > V_MAX

# generate a random vector with elements (temporary)
def generate_a_random_vector():
    newVector = Vector(V_LENGTH)
    for index in range(V_LENGTH):
        randomValue = random.uniform(V_MIN, V_MAX)
        newVector.assign(randomValue, index)
    return newVector

# Bounded uniform convolution main function
def bounded_uniform_convolution():
    print "Bounded Uniform Convolution: "
    # generate a new vector ****INSERT A NEW VECTOR HERE****
    newVector = generate_a_random_vector()
    # print the original vector
    print "\tOriginal vector: " + newVector.toString()
    for index in range(V_LENGTH):
        if P_NOISE >= random.uniform(0.0, 1.0):
            vectorElement = newVector.get(index)
            randomNumber = random.uniform(-R_NOISE, R_NOISE)
            # repeat assigning random number from -R_NOISE to R_NOISE
            while loop_condition_is_met(vectorElement, randomNumber):
                randomNumber = random.uniform(-R_NOISE, R_NOISE)
            # if V_MIN <= vectorElement + randomNumber <= V_MAX,
            newVector.assign(vectorElement + randomNumber, index)
    # print the convoluted vector
    print "\tConvoluted vector: " + newVector.toString()

# execute
bounded_uniform_convolution()
