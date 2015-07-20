# Implementation of Random Search
import random
import math

# domain for the solution
X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed

# function f(x)	****TEST FUNCTION HERE****
def f(x):
    return (6*x-2)**2 * math.sin(12*x-4)

# loop stops when the condition is not met
def loop_condition_is_met(bestSolution, timeCounter):
    timeLimit = 1000
    idealSolution = 15.91
    precision = 0.0001
    return timeCounter < timeLimit and\
         abs(idealSolution - f(bestSolution)) > precision

# main function of Random Search
def random_search():
    # some initial random candidate solution
    bestSolution = random.uniform(X_MIN, X_MAX)
    # time counter that stops when we have run out of time
    timeCounter = 0
    while loop_condition_is_met(bestSolution, timeCounter):
        # a random condidate solution
        randomSolution = random.uniform(X_MIN, X_MAX)
        if f(randomSolution) > f(bestSolution):
            bestSolution = randomSolution
        timeCounter += 1
    # print the best result
    print "Random Search: " +\
            str((round(bestSolution, 3), round(f(bestSolution), 3)))

# execute
random_search()
