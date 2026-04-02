# Install package python-sat !!!
from pysat.solvers import Minisat22
from time import time
from itertools import combinations


def solve_3partition(numbers):
    number_of_triplets = len(numbers) // 3
    target = sum(numbers) // number_of_triplets
    solver = Minisat22()

    valid_triplets = []
    numbers_sorted = sorted(list(numbers))
    n_len = len(numbers_sorted)
    
    for i in range(n_len - 2):
        a = numbers_sorted[i]
        
        # If the smallest number is already greater than or equal to the target,
        # it's impossible to sum to target with positive numbers
        if a >= target:
            break
            
        rem = target - a
        left = i + 1
        right = n_len - 1
        
        while left < right:
            current_sum = numbers_sorted[left] + numbers_sorted[right]
            if current_sum == rem:
                valid_triplets.append((a, numbers_sorted[left], numbers_sorted[right]))
                left += 1
                right -= 1
            elif current_sum < rem:
                left += 1  
            else:
                right -= 1 

    num_valid_triplets = len(valid_triplets)

    # Disjnointness constraint
    for i in range(num_valid_triplets):
        (a,b,c) = valid_triplets[i]
        for j in range(i+1, num_valid_triplets):
            (d,e,f) = valid_triplets[j]
            if a in (d,e,f) or b in (d,e,f) or c in (d,e,f):
                solver.add_clause([-(i+1), -(j+1)])

    # Cover constraint
    for number in numbers:
        clause = []
        for i in range(num_valid_triplets):
            (a,b,c) = valid_triplets[i]
            if number in (a,b,c):
                clause.append(i+1)
        if clause:
            solver.add_clause(clause)

    if solver.solve():
        model = solver.get_model()
        partition = []
        for number in model:
            if number > 0:
                partition.append(valid_triplets[number-1])
        return partition 