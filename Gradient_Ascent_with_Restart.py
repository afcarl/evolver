# Implementation of Gradient Ascent with Restart
import random
import math

X_MIN = -0.20 # minimum x allowed
X_MAX = 1.120 # maximum x allowed
VERY_SMALL_VALUE = 0.0001 # hypothetical small value

# function f(x)	****TEST FUNCTION HERE****
def f(x):
	return (6*x-2)**2 * math.sin(12*x-4)

# calculate the slope of f(x) at x
def f_prime(x):
	return (f(x+VERY_SMALL_VALUE)-f(x))/VERY_SMALL_VALUE

# stop the restart loop when this condition is not met
def first_condition_is_met(x_old, x_new):
	return x_old > X_MIN and x_old < X_MAX and\
			x_new > X_MIN and x_new < X_MAX

# stop the ascent loop when this condition is not met
def second_condition_is_met(x_old, x_new, precision):
	return abs(x_new - x_old) > precision

# Gradient Ascent with Restart main function
def gradient_ascent_with_restart():
	alpha = 0.0001 # step size
	precision = 0.0001 # desired precision
	x_old = 0.0	# initialized x_old
	x_new = random.uniform(X_MIN, X_MAX) # initialized x_new
	x_optimum = x_new # initilaized x_optimum
	timeCounter = 0 # time counter
	timeLimit = 1000 # stop after TIME_LIMIT

	# this process continues until x_old or x_new is out of their range
	while first_condition_is_met(x_old, x_new) and timeCounter < timeLimit:
		# this process continues until the x gives a local peak
		while second_condition_is_met(x_old, x_new, precision):
			x_old = x_new
			x_new = x_old + alpha * f_prime(x_old)
		if f(x_new) > f(x_optimum):
			x_optimum = x_new
		# restart
		x_new = random.uniform(X_MIN, X_MAX)
		# add counter
		timeCounter += 1
	# print the "global" maximum
	print "Gradient Ascent with Restart: " +\
	 		str((round(x_optimum, 3), round(f(x_optimum), 3)))

# execute
gradient_ascent_with_restart()
