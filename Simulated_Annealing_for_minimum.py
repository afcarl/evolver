# Implementation of Simulated Annealing
import random
import math

# domain for the solution
X_MIN = -2.0 # minimum x allowed
X_MAX = 2.0 # maximum x allowed

# function f(x) ****TEST FUNCTIONS HERE****
def f(t_num, x):
    if t_num == 0:
        return (6*x-2)**2 * math.sin(12*x-4)
    elif t_num == 1:
        return -2*(x**3) * math.sin(x**5 + 4)

# loop stops when the condition is not met
def loop_condition_is_met(t, timeCounter, temperature):
    timeLimit = 10000
    return timeCounter < timeLimit and temperature > 0

# check if the given solution is in the provided range
def in_range(solution):
    return solution >= X_MIN and solution <= X_MAX

# randomly tweak the solution
def randomly_tweaked(solution):
    tweakRange = 0.001
    return solution + random.uniform(-tweakRange, tweakRange)

# Simulated Annealing main function
def simulated_annealing(t=0):
    temperature = 100000.0  # initially high temperature
    solution = random.uniform(X_MIN, X_MAX) # some initial candidate solution
    bestSolution = solution
    timeCounter = 0
    while loop_condition_is_met(t, timeCounter, temperature):
        randomSolution = randomly_tweaked(solution)
        p = random.uniform(0.0, 1.0)
        if (f(t,randomSolution) < f(t,solution) or\
            p < math.e**((f(t,randomSolution)-f(t,solution))/temperature)) and\
            in_range(randomSolution):
            solution = randomSolution
        temperature -= 0.01
        if f(t,solution) < f(t,bestSolution):
            bestSolution = solution
        timeCounter += 1
    # print the best solution
    print "Simulated Annealing: " +\
            str((round(bestSolution, 3), round(f(t,bestSolution), 3)))
    # return the best result
    return (round(bestSolution, 3), round(f(t,bestSolution), 3))

# execute
simulated_annealing(0)
