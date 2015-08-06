# Implementation of Genetic Algorithm
import random
import math

X_MIN = -2.0 # minimum x allowed
X_MAX = 2.0 # maximum x allowed
N_POPULATION = 10 # desired population size
P_MUTATION = 0.1 # probability of mutation
P_CROSSOVER = 0.1 # probability of crossover
CHROMOSOME_SIZE = 8 # define the length of binary string

# function f(x) ****TEST FUNCTION HERE****
def f(t_num, chromosome):
    x = inContext(X_MIN, X_MAX, toDecimal(chromosome))
    if t_num == 0:
        return (6*x-2)**2 * math.sin(12*x-4)
    elif t_num == 1:
        return -2*(x**3) * math.sin(x**5+4)
    elif t_num == 2:
        return 3*(x**3) * math.cos(3*(x**3)+3)

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
def loop_condition_is_met(t, timeCounter):
    timeLimit = 1000
    return timeCounter < timeLimit

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

# randomly select two parents from a population
def random_selection(population):
    adam = random.choice(population)
    population.remove(adam)
    eve = random.choice(population)
    population.remove(eve)
    return adam, eve

# uniform crossover that return two children
def uniform_crossover(adam, eve):
    child_1 = "" # first child - adam side
    child_2 = "" # second child - eve side
    for index in range(CHROMOSOME_SIZE):
        chance = random.uniform(0.0, 1.0)
        # if there is a crossover, add exchanged bit to each child
        if chance < P_CROSSOVER:
            child_1 += eve[index]
            child_2 += adam[index]
        # otherwise, add the promised bit to each child
        else:
            child_1 += adam[index]
            child_2 += eve[index]
    return child_1, child_2

# Genetic Algorithm main function
def genetic_algorithm(t=0):
    population = initial_population(N_POPULATION)
    bestGene = "XXXXXXXX" # initially best is nobody
    timeCounter = 0
    while loop_condition_is_met(t, timeCounter):
        for chromosome in population:
            if bestGene == "XXXXXXXX" or f(t,chromosome) < f(t,bestGene):
                bestGene = chromosome
        children = []
        for index in range(N_POPULATION/2):
            adam, eve = random_selection(population)
            child_1, child_2 = uniform_crossover(adam, eve)
            children.append(child_1)
            children.append(child_2)
        population = children
        timeCounter += 1
    # print result
    print "Genetic Algorithm: " + str((bestGene, round(f(t,bestGene), 3)))
    # return result
    return (bestGene, round(f(t,bestGene), 3))

# execute
genetic_algorithm(0)
