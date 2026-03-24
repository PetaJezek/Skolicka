import pandas as pd
from sklearn import metrics
import pylab as pl
import numpy as np
from deap import gp
from deap import algorithms, base, creator, tools

import matplotlib.pyplot as plt


iris = pd.read_csv("iris.csv")

iris.head()



labels = {"Setosa": 0, "Virginica": 1, "Versicolor": 2}
iris_numerical = iris.replace({"variety": labels})


iris_numpy = iris.to_numpy()


iris_x, iris_y = iris_numpy[:,:-1].astype(float), iris_numpy[:,-1].astype("U")

train_to_test_ratio = 4 / 5
num_of_train_samples = int(train_to_test_ratio * len(iris_y))

permutation = np.random.permutation(len(iris_y))
train_idx = permutation[:num_of_train_samples]
test_idx = permutation[num_of_train_samples:]

x_train, x_test = iris_x[train_idx], iris_x[test_idx]
y_train, y_test = iris_y[train_idx], iris_y[test_idx]

print("Number of train samples:", num_of_train_samples, "| Number of test samples:", len(iris_y) - num_of_train_samples)


pset = gp.Primi


# The set of nodes is named "MAIN", input is one float (x), output as well (y)
pset = gp.PrimitiveSetTyped("MAIN", [float], float)

# Rename the first (and in our case only) input argument to "x"
pset.renameArguments(ARG0="x")

# Terminals
pset.addTerminal(1.0, float)
pset.addTerminal(2.0, float)
pset.addTerminal(0.0, float)

# Non-terminals
pset.addPrimitive(np.sin, [float], float) # Here we see that we can use any custom function, not just the predefined ones.
pset.addPrimitive(operator.add, [float, float], float)
pset.addPrimitive(operator.mul, [float, float], float)

# We can add other operators, which are however not used in the original data-generating function.
# We might thusly test the GP's performance in a more "real" setting, where we do not know how
# the data were generated.
# pset.addPrimitive(operator.sub, [float, float], float)
# pset.addPrimitive(np.cos, [float], float)
# pset.addPrimitive(operator.truediv, [float, float], float)

creator.create("FitnessMin", base.Fitness, weights=(-1.0, -0.01))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Setting the algorithm
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, type_=float, min_=3, max_=10)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

toolbox.register("evaluate", fitness, x=x_train, y=y_train)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=1, max_=3)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset) 

# Limits to the tree depth
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))