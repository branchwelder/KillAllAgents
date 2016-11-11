import numpy as np
class Agent:
    def __init__(self, params):
        """Creates a new agent at the given location.
        
        params: dictionary of parameters

        """
        # extract the parameters
        self.health_status = params.get('health_status', 0)
        # Healthy = 0, Sick = 0 Contagious = 0-1.
        

        # How resistent to disease is this agent?
        self.immunity = params.get('immunity', 0.5)
  
