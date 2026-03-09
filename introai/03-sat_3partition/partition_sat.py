# Install package python-sat !!!
from pysat.solvers import Minisat22
from time import time

def solve_3partition(numbers):
    # The following line split given numbers into triples, but their sum is incorrect.
    # Replace it by a correct approach based on SAT.
    return [ list(numbers[i:i+3]) for i in range(0, len(numbers), 3) ]
