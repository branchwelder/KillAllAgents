import numpy as np
class Agent:
    def __init__(self, loc, params):
        """Creates a new agent at the given location.
        
        loc: tuple coordinates where in the grid is the agent located
        params: dictionary of parameters

        Modified from the agent class in ThinkComplexity2 Chapter 9.
        """
        self.loc = tuple(loc)
        self.neighbors = []
        for i in range(self.loc[0] - 1, self.loc[0] + 2):
            for j in range(self.loc[1] - 1, self.loc[1] + 2):
                if (i, j) != self.loc:
                    self.neighbors.append((i, j))

        # extract the parameters
        health_status = params.get('health_status', 2)
        # Healthy = 2, Empty cell = 0 Contagious = 1, Sick = 0.01
        

        # How resistent to disease is this agent?
        min_immunity = params.get('min_immunity', 0.5)
        max_immunity = params.get('max_immunity', 0.8)
        

        # How extroverted is this agent. Does it like to be close to 
        # other agents/the city center?
        urbanness = params.get('urbanness', 0.5)
        
        # choose attributes
        self.health_status = health_status
        self.immunity = np.random.uniform(min_immunity, max_immunity)
        self.urbanness = urbanness

    def step(self, array):
        """ Change health status/other attributes based on environment
        
        array: array representing the city and environment
        """
        
        
        # If sick random chance of getting better 
        if self.health_status == .01:
            # Average sickness duration of ~4 days before being cured (96 timesteps in 4 days)
            if random.randrange(0, 100) == 1:
                self.health_status = 2
            
        # If contagious decrease health status each step until in sick range
        elif self.health_status < 2:
            self.health_status -= .01
        # If healthy:# If contagious decrease health status each step until in sick range
        # If contagious neighbor
        # frac__neighbors_contagious
        # if random integer between (100*frac_neighbors_contagious, 101) > 100* immunity
        # become contagoious
        # else no change
        elif self.health_status >= 2:
            contagious_neighbors = 0
            for neighbor in self.neighbors:
                if array(neighbor).health_status < 2:
                    contagious_neighbors += 1
            if random.randrange(100*(contagious_neighbors/8), 101) > 100 * immunity:
               self.health_status = 1
     

       

