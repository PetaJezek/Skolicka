import numpy, scipy, networkx # You can use everything from these libraries if you find them useful.

"""
    TODO: Improve the strategy controlling the robot.
    You can adopt this file as you like but you have to keep the interface so that your player properly works on recodex; i.e.
        * RobotControl.__init__ is called in for every environment (test).
        * RobotControl.get_command is called to obtain command for movement on a given position.
    Furthermore, calculate_position_distribution is used by tests in the file probability_test.py.
"""

class RobotControl:
    def __init__(self, environment):
        self.env = environment

        # Size of the map
        self.rows = environment.rows
        self.columns = environment.columns

        # The position of the station
        self.destination = environment.destination

        # Map, i.e. a matrix containing color (on grayscale) for every cell
        self.grayscale = environment.grayscale

        # Step counter 
        self.remaining_steps = self.total_steps = environment.steps

        total_valid_cells = (self.rows * self.columns) - 1
        self.position_dist = numpy.full((self.rows, self.columns), 1 / total_valid_cells)
        # Station has 0.0 probability of being the landing site
        dest_r, dest_c = self.destination
        self.position_dist[dest_r][dest_c] = 0.0
        # This is needed only for a trivial control
        self.graph = networkx.grid_2d_graph(self.rows, self.columns)

        self.paths = networkx.single_target_shortest_path(self.graph, self.destination)

        self.spiral_direction = self.env.NORTH
        self.spiral_remains = self.spiral_steps = 1

        self.grayscale_complement = 1 - environment.grayscale

    def get_command(self, sensor_reading):
        self.remaining_steps -= 1
        
        # Aplikuj data ze senzoru a znormalizuj
        self.update_position_by_sensor_reading(sensor_reading)
        self.normalize_position_distribution()
        
        # Odhad polohy
        best_r, best_c = numpy.unravel_index(numpy.argmax(self.position_dist), self.position_dist.shape)
        max_prob = self.position_dist[best_r][best_c]
        
        # Analýza situace s využitím NetworkX
        path_to_goal = self.paths.get((best_r, best_c))
        steps_to_goal = len(path_to_goal) - 1 if path_to_goal else 0
        
        fall_risks = self.get_probabilities_fall()
        
        # ROZHODOVACÍ LOGIKA (State Machine)
        if steps_to_goal - 5 >= self.remaining_steps - 2:
            mode = "EXPLOIT"
        elif max_prob < 0.60:
            mode = "EXPLORE"
        else:
            mode = "EXPLOIT"

        # PROVEDENÍ AKCE
        chosen_command = None
        
        if mode == "EXPLOIT" and steps_to_goal > 0:
            next_node = path_to_goal[1]
            if next_node[0] < best_r: chosen_command = self.env.NORTH
            elif next_node[0] > best_r: chosen_command = self.env.SOUTH
            elif next_node[1] < best_c: chosen_command = self.env.WEST
            else: chosen_command = self.env.EAST
         
            if fall_risks[chosen_command] > 0.35 and steps_to_goal < self.remaining_steps - 2:
                mode = "EXPLORE"
                
        if mode == "EXPLORE" or chosen_command is None:
            spiral_cmd = self.get_command_using_spiral()
            
            # Pokud je spirála bezpečná, uděláme ji. Jinak vybereme absolutně nejbezpečnější krok.
            if fall_risks[spiral_cmd] < 0.35:
                chosen_command = spiral_cmd
            else:
                chosen_command = numpy.argmin(fall_risks) # Zvol směr s nejmenším rizikem pádu

        # Zápis do vnitřní mapy a odeslání příkazu
        self.update_position_by_command(chosen_command)
        return chosen_command
        
    # This is a trivial control in which the robot moves on a spiral.
    # Only for illustrative purposes.
    def get_command_using_spiral(self):
        if self.spiral_remains == 0:
            self.spiral_direction = (self.spiral_direction + 1) % 4
            if self.spiral_direction % 2 == 0:
                self.spiral_steps += 1
            self.spiral_remains = self.spiral_steps
        self.spiral_remains -= 1
        return self.spiral_direction
    
    def update_position_by_sensor_reading(self, sensor_reading):
        if sensor_reading:
            self.position_dist *= self.grayscale
        else:
            self.position_dist *= self.grayscale_complement

    def update_position_by_command(self, command):
        new_position_dist = numpy.zeros((self.rows, self.columns))
        for i in range(self.rows):
            for j in range(self.columns):
                if self.position_dist[i][j] > 0:
                    new_i, new_j = i, j
                    if command == self.env.NORTH:
                        new_i -= 1
                    elif command == self.env.EAST:
                        new_j += 1
                    elif command == self.env.SOUTH:
                        new_i += 1
                    elif command == self.env.WEST:
                        new_j -= 1
                    if 0 <= new_i < self.rows and 0 <= new_j < self.columns:
                        new_position_dist[new_i][new_j] += self.position_dist[i][j]
        self.position_dist = new_position_dist

        dest_r, dest_c = self.destination
        self.position_dist[dest_r][dest_c] = 0.0


    def normalize_position_distribution(self):
        # Normalize the probability distribution of robot's position so that the sum of all probabilities is 1.
        total = self.position_dist.sum()
        if total > 0 and total != 1:
            self.position_dist /= total
    
    def get_probabilities_fall(self):
        fall = [0]*4
        for i in range(self.rows):
            for j in range(self.columns):
                if self.position_dist[i][j] > 0:
                    if i == 0:
                        fall[self.env.NORTH] += self.position_dist[i][j]
                    if j == self.columns - 1:
                        fall[self.env.EAST] += self.position_dist[i][j]
                    if i == self.rows - 1:
                        fall[self.env.SOUTH] += self.position_dist[i][j]
                    if j == 0:
                        fall[self.env.WEST] += self.position_dist[i][j]
        return fall

    # Calculate the probability distribution of robot's position after k steps
    # sensor_readings - a binary array of k+1 sensor readings
    # commands - an array of k robots commands (directions of movements)
    # The robots lands in the environment self.env, sensor reads sensor_readings[0], makes movement commands[0], sensor reads sensor_readings[1], ..., sensor reads sensor_readings[k+1]
    # Determine the probability distribution after these operations.
    # Returns a pair of
    # - a matrix of probability distribution
    # - an array of four probabilities of falling out of map when the robot is moved in corresponding directions 
    def calculate_position_distribution(self, sensor_readings, commands):
        # return (numpy.zeros((self.rows, self.columns)), [0]*4)
        # This is a recommended approach to calculate the probability distribution of robot's position
        for i in range(len(commands)):
            self.update_position_by_sensor_reading(sensor_readings[i])
            self.update_position_by_command(commands[i])
        self.update_position_by_sensor_reading(sensor_readings[-1])
        self.normalize_position_distribution()
        fall = self.get_probabilities_fall()
        return (self.position_dist, fall)
