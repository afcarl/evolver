# Implementation of An Abstract Generational Evolutionary Algorithm
import random
import math

N_POPULATION = 100 # number of population
X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed

# build initial population
def initial_population(n_population):
    population = []
    for index in range(n_population):
        population.append(random.uniform(X_MIN, X_MAX))
    return population

# first step: fitness function f(x) ****TEST FUNCTION HERE****
def assess_fitness(x):
    return (6*x-2)**2 * math.sin(12*x-4)

# second step: breed a new population of children
def breed_population():



# definition of "nobody" is out of range
def is_nobody(best):
    return best < X_MIN or best > X_MAX

# loop stops when the condition is not met
def loop_condition_is_met(best, timeCounter):
    idealSolution = 15.91 # global maximum in the given domain
    timeLimit = 1000 # loop stops after this count
    return idealSolution > assess_fitness(best) and timeCounter < timeLimit

# An Abstract Generational Evolutionary Algorithm main function
def abstract_generational_evolutionary_algorithm(n_population):
    population = initial_population(n_population)
    best = 2 # since best is out of range, it is initially nobody
    timeCounter = 0 # keeps track of time
    while loop_condition_is_met(best, timeCounter):
        for individual in population:
            if is_nobody(best) or\
                assess_fitness(individual) > assess_fitness(best):
                    best = individual


        timeCounter += 1
