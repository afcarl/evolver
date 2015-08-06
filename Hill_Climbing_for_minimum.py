# Implementation of Hill-Climbing
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

# hill climbing loop stops when this condition is not met
def loop_condition_is_met(t, timeCounter):
    timeLimit = 10000
    return timeCounter < timeLimit

def randomly_tweaked(solution):
    tweakRange = 0.001
    return solution + random.uniform(-tweakRange, tweakRange)

# check if the given solution is in the provided range
def in_range(solution):
    return solution >= X_MIN and solution <= X_MAX

# Hill-Climbing main function
def hill_climbing(t=0):
    solution = random.uniform(X_MIN, X_MAX) # some initial candidate solution
    timeCounter = 0 # time counter that increments every loop
    # repeat until S is the ideal solution or we have run out of time
    while loop_condition_is_met(t, timeCounter):
        randomSolution = randomly_tweaked(solution)
        if f(t,randomSolution) < f(t,solution) and in_range(randomSolution):
            solution = randomSolution
        # increment timeCounter
        timeCounter += 1
    # print the "global" solution
    print "Hill-Climbing: " + str((round(solution, 3), round(f(t,solution), 3)))
    # return the solution
    return (round(solution, 3), round(f(t,solution), 3))

# execute
hill_climbing(0)
