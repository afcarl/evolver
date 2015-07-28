# Implementation of Gradient Descent
import random
import math

# constants
X_MIN = -0.20 				# minimum x allowed
X_MAX = 1.120 				# maximum x allowed
VERY_SMALL_VALUE = 0.0001 	# hypothetical small value

# function f(x)	****TEST FUNCTION HERE****
def f(x):
	return (6*x-2)**2 * math.sin(12*x-4)

# calculate the slope of f(x) at x
def f_prime(x):
	return (f(x + VERY_SMALL_VALUE) - f(x)) / VERY_SMALL_VALUE

# stop the descent loop when this condition is not met
def loop_condition_is_met(x_old, x_new, precision):
	return abs(x_new - x_old) > precision and\
			x_old > X_MIN and x_old < X_MAX and\
			x_new > X_MIN and x_new < X_MAX

# Gradient Descent main function
def gradient_descent():
	alpha = 0.0001 							# step size
	precision = 0.0001 						# desired precision
	x_old = 0.0								# initialized x_old
	x_new = random.uniform(X_MIN, X_MAX) 	# random initial vector
	# this process continues until the x reaches
	# a local peak with a given precision
	while loop_condition_is_met(x_old, x_new, precision):
		x_old = x_new
		x_new = x_old - alpha * f_prime(x_old)
	# print the local maximum
	print "Gradient Descent: " + str((round(x_new, 3), round(f(x_new), 3)))

# execute
gradient_descent()
