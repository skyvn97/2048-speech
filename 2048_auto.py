# import the gameplay function, solver and challenger classes
from gameplay import playGame
from py_solver import PySolver as Solver
from cpp_challenger import CppChallenger as Challenger
import sys

# initialize the solver and challenger

solver = Solver("hmm/direction_recognizer.py" if len(sys.argv) < 2 else sys.argv[1])
challenger = Challenger("./random_challenger" if len(sys.argv) < 3 else sys.argv[2])

# play the game
playGame(solver, challenger)
