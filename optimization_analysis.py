# import algorithm implementation
from Gradient_Descent import gradient_descent
from Hill_Climbing_for_minimum import hill_climbing
from Simulated_Annealing_for_minimum import simulated_annealing
from Mu_Lambda_Evolution_Strategy_for_minimum import mu_lambda_evoulution_strategy
from Genetic_Algorithm_for_minimum import genetic_algorithm

# constants
N_TRIAL = 20

# average performance
gradient_descent_average = 0.0
hill_climbing_average = 0.0
simulated_annealing_average = 0.0
mu_lambda_evoulution_strategy_average = 0.0
genetic_algorithm_average = 0.0

# get performance results
for trial in range(N_TRIAL):
    print "**** TRIAL " + str(trial + 1) + " ****"
    gd_x, gd_y = gradient_descent()
    hc_x, hc_y = hill_climbing()
    sa_x, sa_y = simulated_annealing()
    ml_x, ml_y = mu_lambda_evoulution_strategy()
    ga_x, ga_y = genetic_algorithm()

    # sum up the performance result for each algorithm
    gradient_descent_average += gd_y
    hill_climbing_average += hc_y
    simulated_annealing_average += sa_y
    mu_lambda_evoulution_strategy_average += ml_y
    genetic_algorithm_average += ga_y

# calculate average performance
gradient_descent_average /= N_TRIAL
hill_climbing_average /= N_TRIAL
simulated_annealing_average /= N_TRIAL
mu_lambda_evoulution_strategy_average /= N_TRIAL
genetic_algorithm_average /= N_TRIAL

# print average performance
def printAveragePerformance():
    print "**** Average Performance ****"
    print "gDe: " + str(gradient_descent_average)
    print "hCl: " + str(hill_climbing_average)
    print "sAn: " + str(simulated_annealing_average)
    print "mLa: " + str(mu_lambda_evoulution_strategy_average)
    print "gAl: " + str(genetic_algorithm_average)
