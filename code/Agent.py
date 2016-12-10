import numpy as np
class Agent:
    def __init__(self, **params):
        """Creates a new agent at the given location.

        params: dictionary of parameters

        """
        self.recovered = False

        # extract the parameters

        # How sick is this agent?
        # Healthy = 0, Sick = 1, Contagious = 0-1
        self.health = params.get('health', 0)

        # How resistent to disease is this agent?
        self.immunity = params.get('immunity', 0.5)

        # How extroverted is this agent?
        # Introverted = 0, Extroverted = 1, Range between
        self.social = 0#np.random.random()
