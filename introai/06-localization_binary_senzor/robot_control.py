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

        self.total_valid_cells = (self.rows * self.columns) - 1
        self.position_dist = numpy.full((self.rows, self.columns), 1 / self.total_valid_cells)
        # Station has 0.0 probability of being the landing site
        dest_r, dest_c = self.destination
        self.position_dist[dest_r][dest_c] = 0.0
        

        self.spiral_direction = self.env.NORTH
        self.spiral_remains = self.spiral_steps = 1

        self.grayscale_complement = 1 - environment.grayscale

        self.start = [self.env.NORTH, self.env.SOUTH, self.env.EAST, self.env.WEST]
        self.start_index = 0
        

        base_risk_ns = 1.0 / self.rows
        base_risk_ew = 1.0 / self.columns
        # Vezmeme tu horší (větší) variantu
        max_base_risk = max(base_risk_ns, base_risk_ew)
        self.k = max_base_risk + 0.1

    def get_command(self, sensor_reading):
        
        ScaryCommands = []
        # Spocitej pravdepobnost ze spadneme po kazdem smeru
        for command in [self.env.NORTH, self.env.EAST, self.env.SOUTH, self.env.WEST]:
            fall_prob = self.get_probabilities_fall()[command]
            if fall_prob > self.k:
                ScaryCommands.append(command)
        
        # Hloupa Helper funkce pro vyber nejlepsiho pohybu pro dany bod
        # Bereme v potaz i nebezpecnost pohybu, t.j. nebudeme se snazit jit do smeru, ktery by nas mohl posunout mimo mapu
        def BestMove(target_r, target_c):
            best_command = None
            best_distance = self.rows * self.columns

            safe_commands = set([self.env.NORTH, self.env.EAST, self.env.SOUTH, self.env.WEST]) - set(ScaryCommands)

            if not safe_commands:
                fall_probs = self.get_probabilities_fall()
                # Vrací index (příkaz) s nejmenším rizikem
                return min(range(4), key=lambda c: fall_probs[c])
            
            else:
                for command in safe_commands:
                    new_r, new_c = target_r, target_c
                    if command == self.env.NORTH:
                        new_r -= 1
                    elif command == self.env.EAST:
                        new_c += 1
                    elif command == self.env.SOUTH:
                        new_r += 1
                    elif command == self.env.WEST:
                        new_c -= 1
                    if 0 <= new_r < self.rows and 0 <= new_c < self.columns:
                        distance = abs(new_r - self.destination[0]) + abs(new_c - self.destination[1])
                        if distance < best_distance:
                            best_distance = distance
                            best_command = command
            return best_command
    
        self.remaining_steps -= 1
        
        # Aplikuj data ze senzoru a znormalizuj
        self.update_position_by_sensor_reading(sensor_reading)
        self.normalize_position_distribution()
        
        # Odhad polohy
        best_r, best_c = numpy.unravel_index(numpy.argmax(self.position_dist), self.position_dist.shape)
        max_prob = self.position_dist[best_r][best_c]

        # Pocet kroku od nejlepsiho odhadu k cilovemu bodu
        dist_to_destination = abs(best_r - self.destination[0]) + abs(best_c - self.destination[1])
        
        # Nase nejlepsi pravdepodobnost je stale zla, takze udelame nejbezpecnejsi pohyb po  spirale abychom ziskali data pro lepsi odhad
        if max_prob < 0.1:
            chosen_command = self.start[self.start_index]
            self.start_index = (self.start_index + 1) % len(self.start)
        elif max_prob < 0.4:
            chosen_command = self.spiral_direction
            self.spiral_remains -= 1
            if self.spiral_remains == 0:
                # Změna směru ve spirále
                if self.spiral_direction == self.env.NORTH and self.env.NORTH not in ScaryCommands:
                    self.spiral_direction = self.env.EAST
                elif self.spiral_direction == self.env.EAST and self.env.EAST not in ScaryCommands:
                    self.spiral_direction = self.env.SOUTH
                elif self.spiral_direction == self.env.SOUTH and self.env.SOUTH not in ScaryCommands:
                    self.spiral_direction = self.env.WEST
                elif self.spiral_direction == self.env.WEST and self.env.WEST not in ScaryCommands:
                    self.spiral_direction = self.env.NORTH
                # Po kolecku zvetusjeme kroky
                # if self.spiral_direction in [self.env.NORTH]:
                #     self.spiral_steps += 1
                self.spiral_remains = self.spiral_steps
        elif dist_to_destination + self.total_steps * 0.15 >= self.remaining_steps and max_prob > 0.4: 
            # Pokud nám zbývá málo kroků, jdeme přímo k cíli
            chosen_command = BestMove(best_r, best_c)
        elif max_prob < 0.7:
            # Vybereme body ktere maji pravdepodobnost blizko maximalni pravdepodobnosti
            # a z nich nahodne vybereme jeden podle skalovane pravdepodobnosti a i jeho nejelpsi tah
            candidates = []
            for i in self.position_dist.flatten().argsort()[::-1]:
                r, c = numpy.unravel_index(i, self.position_dist.shape)
                # Bereme jen ty, jejichz pravdepodobnost se lisi jen o 10% od 
                if self.position_dist[r,c] < max_prob * 0.9:
                    break
                candidates.append(((r, c), self.position_dist[r][c]))
            # pick one candidate based on their probabilities
            total_prob = sum(prob for _, prob in candidates)
            if total_prob > 0:
                candidates = [(pos, prob / total_prob) for pos, prob in candidates]
                chosen_pos = numpy.random.choice(len(candidates), p=[prob for _, prob in candidates])
                best_r, best_c = candidates[chosen_pos][0]
                # choose the best move towards the chosen position
                chosen_command = BestMove(best_r, best_c)

        else:
            # Jinak jdeme k nejpravdepodobnejsimu bodu
            chosen_command = BestMove(best_r, best_c)
        # Zápis do vnitřní mapy a odeslání příkazu
        self.update_position_by_command(chosen_command)
        return chosen_command
        
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
