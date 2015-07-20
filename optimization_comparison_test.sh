clear
echo "************************************************************************"
echo "             **** OPTIMIZATION VIA SEARCH FOR MAXIMUM ****              "
echo "f(x) = (6x - 2)^2 * sin(12x - 4)"
echo "from -0.20 to 1.120:"
echo "LOCAL:    (-0.091, 6.021), (0.333, 0), (0.524, 0.986), (1.008, 15.91)"
echo "\"GLOBAL\": (1.008, 15.91)"
echo "************************************************************************"
python Gradient_Ascent.py
python Newtons_Method.py
python Gradient_Ascent_with_Restart.py
python Hill-Climbing.py
python Steepest_Ascent_Hill-Climbing.py
python Steepest_Ascent_Hill-Climbing_with_Replacement.py
python Random_Search.py
python Hill-Climbing_with_Random_Restarts.py
python Simulated_Annealing.py
python Mu_Lambda_Evolution_Strategy.py
echo ""
echo "************************************************************************"
echo "          RANDOM GENERATION OF VECTORS AND THEIR CONVOLUTION            "
echo "************************************************************************"
python Generate_a_Random_Real-Valued_Vector.py
python Bounded_Uniform_Convolution.py
python Gaussian_Convolution.py
python Box-Muller-Marsaglia_Polar_Method.py
