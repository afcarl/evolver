# Implementation of Simulated Annealing
import random
import math

# domain for the solution
X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed

# function f(x) ****TEST FUNCTION HERE****
def f(x):
    return (6*x-2)**2 * math.sin(12*x-4)

# loop stops when the condition is not met
def loop_condition_is_met(bestSolution, timeCounter, temperature):
    idealSolution = -6.02
    precision = 0.0001
    timeLimit = 1000000
    return abs(idealSolution - f(bestSolution)) > precision and\
            timeCounter < timeLimit and temperature > 0

# randomly tweak the solution
def randomly_tweaked(solution):
    tweakRange = 0.001
    return solution + random.uniform(-tweakRange, tweakRange)

# Simulated Annealing main function
def simulated_annealing():
    temperature = 100000.0  # initially high temperature
    solution = random.uniform(X_MIN, X_MAX) # some initial candidate solution
    bestSolution = solution
    timeCounter = 0
    while loop_condition_is_met(bestSolution, timeCounter, temperature):
        randomSolution = randomly_tweaked(solution)
        p = random.uniform(0.0, 1.0)
        if f(randomSolution) > f(solution) or\
            p < math.e**((f(randomSolution)-f(solution))/temperature):
            solution = randomSolution
        temperature -= 0.01
        if f(solution) < f(bestSolution):
            bestSolution = solution
        timeCounter += 1
    # print the best solution
    print "Simulated Annealing: " +\
            str((round(bestSolution, 3), round(f(bestSolution), 3)))

# execute
simulated_annealing()
