# Implementation of Hill-Climbing with Random Restarts
import random
import math

# constants
X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed
T_MAX = 1000 # total maximum time

# function f(x) ****TEST FUNCTION HERE****
def f(x):
    return (6*x-2)**2 * math.sin(12*x-4)

# loop stops when the condition is not met
def loop_condition_is_met(solution, timeCounter, time=T_MAX):
    idealSolution = 15.91
    precision = 0.0001
    return timeCounter < time and\
         abs(idealSolution - f(solution)) > precision

def randomly_tweaked(solution):
    tweakRange = 0.001
    return solution + random.uniform(-tweakRange, tweakRange)

# Hill-Climbing with Random Restarts main function
def hill_climbing_with_random_restarts():
    # some initial random candidate solution
    solution = random.uniform(X_MIN, X_MAX)
    # initialize best solution
    bestSolution = solution
    # global time counter that increments every loop
    timeCounter = 0
    while loop_condition_is_met(bestSolution, timeCounter):
        # random time in the near future between timeCounter and T_MAX
        time = random.randint(timeCounter, T_MAX)
        while loop_condition_is_met(solution, timeCounter, time):
            randomSolution = randomly_tweaked(solution)
            if f(randomSolution) > f(solution):
                solution = randomSolution
            # increment local/global time
            timeCounter += 1
        if f(solution) > f(bestSolution):
            bestSolution = solution
        solution = random.uniform(X_MIN, X_MAX)
    # print the best solution
    print "Hill Climbing with Random Restarts: " +\
            str((round(bestSolution, 3), round(f(bestSolution), 3)))

# execute
hill_climbing_with_random_restarts()
