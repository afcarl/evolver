# Implementation of Gradient Descent
import random
import math

# constants
X_MIN = -2.0 				# minimum x allowed
X_MAX = 2.0 				# maximum x allowed
VERY_SMALL_VALUE = 0.0001 	# hypothetical small value

# function f(x) ****TEST FUNCTIONS HERE****
def f(t_num, x):
    if t_num == 0:
        return (6*x-2)**2 * math.sin(12*x-4)
    elif t_num == 1:
        return -2*(x**3) * math.sin(x**5 + 4)

# calculate the slope of f(x) at x
def f_prime(t,x):
	return (f(t,x + VERY_SMALL_VALUE) - f(t,x)) / VERY_SMALL_VALUE

# stop the descent loop when this condition is not met
def loop_condition_is_met(x_old, x_new, precision, timeCounter):
	timeLimit = 10000
	return abs(x_new - x_old) > precision and\
			x_old > X_MIN and x_old < X_MAX and\
			x_new > X_MIN and x_new < X_MAX and\
			timeCounter < timeLimit

# Gradient Descent main function
def gradient_descent(t=0):
	alpha = 0.0001 							# step size
	precision = 0.0001 						# desired precision
	x_old = 0.0								# initialized x_old
	x_new = random.uniform(X_MIN, X_MAX) 	# random initial vector
	timeCounter = 0							# time counter
	# this process continues until the x reaches
	# a local peak with a given precision
	while loop_condition_is_met(x_old, x_new, precision, timeCounter):
		x_old = x_new
		x_new = x_old - alpha * f_prime(t,x_old)
		timeCounter += 1
	# print the local minimum
	print "Gradient Descent: " + str((round(x_new, 3), round(f(t,x_new), 3)))
	# return the local minimum
	return (round(x_new, 3), round(f(t,x_new), 3))

# execute
gradient_descent(0)
