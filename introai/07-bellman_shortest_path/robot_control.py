import numpy, scipy, networkx # You can use everything from these libraries if you find them useful.
import scipy.sparse as sparse # Calling scipy.sparse.csc_matrix does not work on Recodex, so call sparse.csc_matrix(...) instead
import scipy.sparse.linalg as linalg # Also, call linalg.spsolve

"""
    TODO: Improve the strategy controlling the robot.
    A recommended approach is implementing the function RobotControl.precompute_distance_policy.
    You can adopt this file as you like but you have to keep the interface so that your player properly works on recodex; i.e.
        * RobotControl.__init__ is called in for every environment (test).
        * RobotControl.get_command is called to obtain command for movement on a given position.
    Furthermore, get_distance and get_policy is used by tests in the file probability_test.py and get_policy_from_distance and get_distance_from_policy by policy_iteration_test.py.
"""

class RobotControl:
    def __init__(self, environment):
        self.env = environment
        self.distance,self.policy = self.precompute_distance_policy()

    # Returns a matrix of maximal probabilities of reaching the station from every cell
    def get_distance(self):
        return self.distance

    # Returns a matrix of commands for every cell
    def get_policy(self):
        return self.policy

    # Returns command for movement from the current position.
    # This function is called quite a lot of times, so it is recommended to avoid any heavy computation here.
    def get_command(self, current):
        return self.policy[tuple(current)]


    # Place all your precomputation here.
    def precompute_distance_policy(self):
        env = self.env

        current_policy = numpy.zeros((env.rows, env.columns), dtype=int)
        current_distance = numpy.zeros((env.rows, env.columns))


        while True:
            current_distance = self.get_distance_from_policy(current_policy)
            
            new_policy = self.get_policy_from_distance(current_distance)
            
            if numpy.array_equal(new_policy, current_policy):
                break
                
            current_policy = new_policy

        return current_distance, current_policy

    # Returns a trivial control strategy which just heads directly toward the station ignoring all dangers and movement imperfectness
    def precompute_distance_policy_trivial(self):
        env = self.env
        distance = numpy.zeros((env.rows, env.columns)) # No probability is computed
        policy = self.get_policy_from_distance(distance)
        for i in range(env.rows):
            for j in range(env.columns):
                if i > env.destination[0]:
                    policy[i,j] = env.NORTH
                elif i < env.destination[0]:
                    policy[i,j] = env.SOUTH
                elif j < env.destination[1]:
                    policy[i,j] = env.EAST
                elif j > env.destination[1]:
                    policy[i,j] = env.WEST
        return distance, policy
    
    # Returns the optimal policy for given distances
    def get_policy_from_distance(self, distance):
        env = self.env
        policy = numpy.zeros((env.rows, env.columns), dtype=int)
        for i in range(env.rows):
            for j in range(env.columns):
                current_pos = tuple([i,j])
                if current_pos == tuple(env.destination):
                                    continue
                min_expected_energy = float('inf')
                best_command = -1

                # calculated expected energy for every command and rotation and choose the best one
                for command in range(4):
                    expected_energy = 0.0
                
                    for rotation in range(4):
                        next_pos = env.get_position_after_action(current_pos, command, rotation)
                        cost = env.get_energy(next_pos)                        
                        remaining_dist = distance[next_pos]                        
                        prob = env.rotation_probability[rotation]
                        expected_energy += prob * (cost + remaining_dist)
                    
                    # If this command's expected energy is the lowest we've seen, save it!
                    if expected_energy < min_expected_energy:
                        min_expected_energy = expected_energy
                        best_command = command
                
                # Assign the winning command to this cell in our policy grid
                policy[i, j] = best_command
                
        
        return policy
    
    # Returns the optimal distances for given policy
    def get_distance_from_policy(self, policy):
        env = self.env
        distance = numpy.zeros((env.rows, env.columns))
        total_cells = env.rows * env.columns

        A_row = []
        A_col = []
        A_data = []

        b = numpy.zeros(total_cells)

        for i in range(env.rows):
            for j in range(env.columns):
                s = i * env.columns + j  

                # if this is cell the is the station
                if (i, j) == tuple(env.destination):
                    A_row.append(s)
                    A_col.append(s)
                    A_data.append(1.0)
                    b[s] = 0.0
                    continue

                A_row.append(s)
                A_col.append(s)
                A_data.append(1.0)

                command = policy[i, j]
                expected_energy = 0.0


                for rotation in range(4):
                    next_pos = env.get_position_after_action((i, j), command, rotation)
                    cost = env.get_energy(next_pos)
                    prob = env.rotation_probability[rotation]
                    next_s = next_pos[0] * env.columns + next_pos[1] 

                    A_row.append(s)
                    A_col.append(next_s)
                    A_data.append(-prob)

                    expected_energy += prob * cost

                b[s] = expected_energy
        
        A = sparse.csc_matrix((A_data, (A_row, A_col)), shape=(total_cells, total_cells))
        distance_vector = linalg.spsolve(A, b)
        distance = distance_vector.reshape((env.rows, env.columns))


        return distance

