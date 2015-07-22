# Implementation of Genetic Algorithm
import random
import math

X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed
N_POPULATION = 20 # desired population size
P_MUTATION = 0.1 # probability of mutation
P_CROSSOVER = 0.3 # probability of crossover
CHROMOSOME_SIZE = 4 # define the length of binary string

# function f(x) ****TEST FUNCTION HERE****
def f(chromosome):
    x = inContext(X_MIN, X_MAX, toDecimal(chromosome))
    return (6*x-2)**2 * math.sin(12*x-4)

# generate initial population
def initial_population(n_population):
    population = []
    for p_index in range(n_population):
        chromosome = ""
        for c_index in range(CHROMOSOME_SIZE):
            chromosome += random.choice(["0", "1"])
        population.append(chromosome)
    return population

# loop stops when the condition is not met
def loop_condition_is_met(bestGene, timeCounter):
    timeLimit = 10
    idealSolution = 15.91
    precision = 0.001
    return abs(idealSolution - f(bestGene)) > precision and\
            timeCounter < timeLimit

# convert the binary into decimal
def toDecimal(binaryString):
    decimalNumber = 0
    length = len(binaryString)
    for index, digit in enumerate(binaryString):
        if digit == "1":
            decimalNumber += 2**(length - index - 1)
    return decimalNumber

# convert the decimal number into real value in context
def inContext(x_min, x_max, decimal):
    r_min = 0.0
    r_max = 2**CHROMOSOME_SIZE-1
    precision = (x_max - x_min) / (r_max - r_min)
    return x_min + decimal * precision

# mutate each index of a chromosome with a chance of P_MUTATION
def mutated(chromosome):
    mutatedChromosome = ""
    for index in range(CHROMOSOME_SIZE):
        if random.uniform(0.0, 1.0) < P_MUTATION:
            if chromosome[index] == "0":
                mutatedChromosome += "1"
            elif chromosome[index] == "1":
                mutatedChromosome += "0"
        else:
            mutatedChromosome += chromosome[index]
    return mutatedChromosome

# Genetic Algorithm main function
def genetic_algorithm():
    population = initial_population(N_POPULATION)
    bestGene = "XXXX" # initially best is nobody
    



# execute
genetic_algorithm()
