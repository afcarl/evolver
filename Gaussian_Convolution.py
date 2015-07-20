# Implementation of Gaussian Convolution
import random
import math

# constants
V_MIN = 0.0 # minimum desired vector element value
V_MAX = 10.0 # maximum desired vector element value
V_LENGTH = 10 # vector length
P_NOISE = 1.0 # probability of adding noise to an element in the vector
MU = 0.0 # mean of the Normal distribution
SIGMA = 0.5 # standard deviation of the Normal distribution

# define vector class
class Vector:
    # initialize the container for vector
    def __init__(self, length=10):
        self.vectorLength = length
        self.vectorContainer = [0] * self.vectorLength
    # return an element of the vector at given index
    def getElement(self, index):
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

# generate a random vector with elements (temporary)
def generate_a_random_vector(vectorLength=10):
    newVector = Vector(vectorLength)
    for index in range(vectorLength):
        randomValue = random.uniform(V_MIN, V_MAX)
        newVector.assign(randomValue, index)
    return newVector

# loop stops when the condition is not met
def loop_condition_is_met(vectorElement, noise):
    return vectorElement + noise < V_MIN and vectorElement + noise > V_MAX

# Gaussian Convolution main function
def gaussian_convolution():
    print "Gaussian Convolution: "
    # generate a new vector ****INSERT A NEW VECTOR HERE****
    vector = generate_a_random_vector(V_LENGTH)
    # print the original vector
    print "\tOriginal vector: " + vector.toString()
    for index in range(V_LENGTH):
        if P_NOISE >= random.uniform(0.0, 1.0):
            # random number chosen from the Normal distribution N(0, SIG_SQ)
            noise = random.gauss(MU, SIGMA)
            # loop until min < vectorElement + n < max
            while loop_condition_is_met(vector.getElement(index), noise):
                noise = random.gauss(MU, SIGMA)
            vector.assign(vector.getElement(index) + noise, index)
    # print the convoluted vector
    print "\tConvoluted vector: " + vector.toString()

# execute
gaussian_convolution()
