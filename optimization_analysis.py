# import algorithm implementation
from Gradient_Descent import gradient_descent
from Hill_Climbing_for_minimum import hill_climbing
from Simulated_Annealing_for_minimum import simulated_annealing
from Mu_Lambda_Evolution_Strategy_for_minimum import mu_lambda_evoulution_strategy
from Genetic_Algorithm_for_minimum import genetic_algorithm

# constants
N_TRIAL = 20
F1 = 0      # f(x) = (6x - 2)^2 * sin(12x - 4)
F2 = 1      # f(x) = -2x^3 * sin(x^5 + 4)
F3 = 2      # f(x) = 3x^3 * cos(3x^3 + 3)

# print test function
def print_test_function(test_number):
    if test_number == 0:
        return "f(x) = (6x - 2)^2 * sin(12x - 4)\n"
    elif test_number == 1:
        return "f(x) = -2x^3 * sin(x^5 + 4)\n"
    elif test_number == 2:
        return "f(x) = 3x^3 * cos(3x^3 + 3)\n"

# print average performance
def printAveragePerformance(test_number):
    # average performance
    gradient_descent_average = 0.0
    hill_climbing_average = 0.0
    simulated_annealing_average = 0.0
    mu_lambda_evoulution_strategy_average = 0.0
    genetic_algorithm_average = 0.0

    # get performance results
    for trial in range(N_TRIAL):
        print "**** TRIAL " + str(trial + 1) + " ****"
        gd_x, gd_y = gradient_descent(test_number)
        hc_x, hc_y = hill_climbing(test_number)
        sa_x, sa_y = simulated_annealing(test_number)
        ml_x, ml_y = mu_lambda_evoulution_strategy(test_number)
        ga_x, ga_y = genetic_algorithm(test_number)

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
    return "**** Average Performance ****\n" +\
            print_test_function(test_number) +\
            "gDe: " + str(gradient_descent_average) + "\n" +\
            "hCl: " + str(hill_climbing_average) + "\n" +\
            "sAn: " + str(simulated_annealing_average) + "\n" +\
            "mLa: " + str(mu_lambda_evoulution_strategy_average) + "\n" +\
            "gAl: " + str(genetic_algorithm_average) + "\n\n"

result_file = open("analysis_result", "w")
result_file.write(printAveragePerformance(0))
result_file.write(printAveragePerformance(1))
result_file.write(printAveragePerformance(2))
