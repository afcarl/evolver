# Implementation of Box-Muller-Marsaglia Polar Method
# Sample from the Gaussian Distribution
import random
import math

MU = 0.0 # desired mean of the Normal distribution
SIGMA = 0.5 # desired standard deviation of the Normal distribution
SIG_SQ = SIGMA**2 # desired variance of the Normal distribution

# loop stops when the condition is not met
def loop_condition_is_met(w):
    return w <= 0 and w >= 1

# Box-Muller-Marsaglia Polar Method main function
def box_muller_marsaglia_polar_method(MU, SIG_SQ):
    # random number chosen uniformly from -1.0 to 1.0
    x = random.uniform(-1.0, 1.0)
    # random number chosen uniformly from -1.0 to 1.0
    y = random.uniform(-1.0, 1.0)
    w = x**2 + y**2
    # loop until w is not 0 or negative
    while loop_condition_is_met(w):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        w = x**2 + y**2
    # two random Gaussian numbers
    g = MU + x * SIGMA * math.sqrt(-2 * math.log(w) / w)
    h = MU + y * SIGMA * math.sqrt(-2 * math.log(w) / w)
    # print the two random numbers
    print "Box-Muller-Marsaglia Polar Method: " +\
            str((round(g, 3), round(h, 3)))

# execute
box_muller_marsaglia_polar_method(MU, SIG_SQ)
