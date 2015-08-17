# Implementation of Gradient Descent
import random
import math

# constants
X_MIN = -2.0 				# minimum x allowed
X_MAX = 2.0 				# maximum x allowed
VERY_SMALL_VALUE = 0.0001 	# hypothetical small value

# function f(v) ****TEST FUNCTIONS HERE****
# *parameter v is independent variables vector
def f(t_num, v):
    if t_num == 0:
        x1 = v[0]
        return (6*x-2)**2*math.sin(12*x-4)
    elif t_num == 1:
        x1 = v[0]
        x2 = v[1]
        return (x2-(5.1/(4*math.pi**2))*(x1**2)+5*x1/math.pi-6)**2+\
                10*(1-1/(8*math.pi))*math.cos(x1)+10
    elif t_num == 2:
        x1 = v[0]
        x2 = v[1]
        return 

# calculate the slope of f(x) at x
def f_prime(t,x):
	return (f(t,x + VERY_SMALL_VALUE) - f(t,x)) / VERY_SMALL_VALUE

# calculate derivative of vector v
def f_prime(t, v):
    v_prime = []
    for component in v:
        v_prime.append(f_prime(t, component))
    return v_prime

# stop the descent loop when this condition is not met
def loop_condition_is_met(x_old, x_new, precision, timeCounter):
	timeLimit = 10000
	return abs(x_new - x_old) > precision and\
			x_old > X_MIN and x_old < X_MAX and\
			x_new > X_MIN and x_new < X_MAX and\
			timeCounter < timeLimit

# Gradient Descent main function
def gradient_descent(t=0, n_var=1):
	alpha = 0.0001 							# step size
	precision = 0.0001 						# desired precision
	x_old = []								# initialized x_old vector
    # generate a random vector
	x_new = []
    for index in range(n_var):
        x_new.append(random.uniform(X_MIN, X_MAX))
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
