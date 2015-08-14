# import algorithm implementation
from Gradient_Descent import gradient_descent
from Hill_Climbing import hill_climbing
from Simulated_Annealing import simulated_annealing
from Mu_Lambda_Evolution_Strategy import mu_lambda_evoulution_strategy
from Genetic_Algorithm import genetic_algorithm

# TEST FUNCTIONS
# 1) One variable function: 2*sin(6x-2) * (6x-2)^2, 0<=x<=1
# 2) Branin function:
# 3) Rosenbrock (-5<= x_i <= 5)
# 4) Goldstein-Price (-2<= x_i <= 2).

# constants
N_TRIAL = 20
F1 = 0  # f(x)=(6x-2)^2*sin(12x-4)
F2 = 1  # f(x)=(x2-(5.1/4pi^2)x1^2+5x1/pi-6)^2+10(1-1/8pi)cos(x1)+10


# print test function
def print_test_function(test_number):
    if test_number == 0:
        return "f(x)=(6x-2)^2*sin(12x-4)\n"
    elif test_number == 1:
        return "f(x)=(x2-(5.1/4pi^2)x1^2+5x1/pi-6)^2+10(1-1/8pi)cos(x1)+10\n"
    elif test_number == 2:
        return ""
    elif test_number == 3:
        return ""

# print average performance
def printAveragePerformance(test_number, n_var):
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
        ml_x, ml_y = mu_lambda_evoulution_strategy(test_number, n_var)
        ga_x, ga_y = genetic_algorithm(test_number, n_var)
        print "\n"

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

print "Writing file to \"analysis_result\"..."
result_file = open("analysis_result", "w")
result_file.write(printAveragePerformance(0, 1))
result_file.write(printAveragePerformance(1, 1))
result_file.write(printAveragePerformance(2, 1))
print "Writing file complete."
