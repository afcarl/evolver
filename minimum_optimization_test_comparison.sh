#!/bin/bash
clear
echo "Test problem: f(x) = (6x - 2)^2 * sin(12x - 4)"
for i in {1..20}
    do
        echo "*****TRIAL $i*****"
        python Gradient_Descent.py
        python Hill-Climbing_for_minimum.py
        python Simulated_Annealing_for_minimum.py
        python Mu_Lambda_Evolution_Strategy_for_minimum.py
        python Genetic_Algorithm_for_minimum.py
    done
