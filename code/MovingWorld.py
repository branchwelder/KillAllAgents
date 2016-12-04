
from __future__ import print_function, division


import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt

import thinkplot
from thinkstats2 import Cdf
from thinkstats2 import RandomSeed

from matplotlib import rc
rc('animation', html='html5')

from Cell2D import Cell2D, Cell2DViewer
import random
from Agent import Agent
from World import World
from WorldViewer import WorldViewer
import copy
from copy import deepcopy
import math

def distance(x, y):
    """Helper function for initializing each cell in the array with
    a distance from the city center.
    """
    x_dist = abs(x-city_center)
    y_dist = abs(y-city_center)
    return np.sqrt(x_dist**2 + y_dist**2)


def city_init(n=100):
    """Returns two arrays:
        arr: represents the city, with the city center holding the highest value
        agents: represents the placement of the agents, randomly assigned based
        on their extroversion attributes
    """
    global city_center
    city_center = n//2
    dist_arr = np.fromfunction(distance,(n,n))

    #normalize so city center is in the middle of the array
    dist_arr = np.amax(dist_arr) - dist_arr
    dist_arr = dist_arr/np.amax(dist_arr)

    return dist_arr

class MovingWorld(Cell2D):
    """
    Represents a world of sick and healthy agents.
        n: dimension of array
        num_agents: number of agents in array
        num_sick: number of agents who are sick
        moves_per_step: number of moves per step in simulation
        sick_move: boolean of whether or not sick agents move

    """

    def __init__(self, agent_array=None, **params):
        """Creates agent array and places agents and initializes parameters.
        """

        # Initialize world parameters
        self.n = params.get("n", 10)
        self.num_population = params.get("num_agents", self.n**2)
        self.num_sick = params.get("num_sick", 1)
        self.num_moves = params.get("moves_per_step", 0)
        self.sick_move = params.get("sick_move", False)

        # Initialize arrays to track illness data
        self.healthy = []
        self.contagious = []
        self.sick = []

        # Populate agent array if not passed in existing array
        if agent_array == None:
            # Create an n by n grid filled with Nones
            self.agent_array = [[None for x in range(self.n)] for y in range(self.n)]

            # Create lists to track illness statuses of agents
            sick_list = [1 for _ in range(self.num_sick)]
            healthy_list = [0 for _ in range(self.num_population - self.num_sick)]
            empty_list = [None for _ in range (self.n**2 - self.num_population)]

            health_shuffle = sick_list + healthy_list + empty_list
            random.shuffle(health_shuffle)

            # Place agents
            for i in range(self.n):
                for j in range(self.n):
                    if isinstance(health_shuffle[self.n * i + j], (int, float)):
                        self.agent_array[i][j] = Agent(health=health_shuffle[self.n * i + j])
        else:
            self.agent_array = agent_array

        # Initialize occupancy grid to keep track of agent presence
        self.occupancy_grid = np.zeros((self.n, self.n))
        for x in range(self.n):
            for y in range(self.n):
                if self.agent_array[i][j] is not None:
                    # Set occupied locations to one
                    self.occupancy_grid[i][j] = 1

        # Create an agent health visualization array
        self.array = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                if self.agent_array[i][j] is not None:
                    self.array[i][j] = self.agent_array[i][j].health + 1


    # Every step represents the change in one hour
    def step(self):

        # Loop through agent objects and update based on params
        new_agent_array = deepcopy(self.agent_array)

        for i in range(self.n):
            for j in range(self.n):
                if self.agent_array[i][j] is not None:
                    #print("Cell: " + str((i, j)))
                    # Get list of neighbors health
                    neighbors_health = []
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 2):
                            if (a, b) != (i, j) and a >= 0 and a < self.n and b >= 0 and b < self.n:
                                if self.agent_array[a][b] is not None:
                                    neighbors_health.append(self.agent_array[a][b].health)

                    # Get fraction of neighbors that are sick
                    neigh_health_frac = sum(neighbors_health) / 8

                    # Update agent health
                    # If sick (and contagious)
                    if self.agent_array[i][j].health > 0.9:
                        if random.randrange(0, 100) == 1:
                            new_agent_array[i][j].recovered = True
                            new_agent_array[i][j].health = 0

                    # If health and contagious
                    elif self.agent_array[i][j].health < 1 and self.agent_array[i][j].health > 0:
                        #print("I was contagious")
                        new_agent_array[i][j].health += 0.1

                    # If healthy
                    elif self.agent_array[i][j].health == 0:
                        immunity = self.agent_array[i][j].immunity
                        neigh_health_chance = neigh_health_frac
                        health_chance = random.random() * neigh_health_chance * 5
                        if self.agent_array[i][j].recovered == True:
                            new_agent_array[i][j].health = 0
                        elif neigh_health_chance == 0:
                            new_agent_array[i][j].health = 0
                        elif health_chance > immunity:
                            new_agent_array[i][j].health = 0.1


        empty = self.array == 0
        occupied = self.array > 0
        empty_locs = np.transpose(np.nonzero(empty))
        occupied_locs = np.transpose(np.nonzero(occupied))

        if len(occupied_locs):
            np.random.shuffle(occupied_locs)
        if len(empty_locs):
            np.random.shuffle(empty_locs)

            if self.num_moves > len(occupied_locs) or self.num_moves > len(occupied_locs):
                self.num_moves = min(len(occupied_locs),len(empty_locs))


            for i in range(self.num_moves):
                source = occupied_locs[i]
                source_i, source_j = tuple(source)
                dest_i, dest_j = tuple(empty_locs[i])

                # Check if agent is healthy(or contagious but not sick) and if sick agents moving is true
                if self.array[source_i][source_j] < 2 or self.sick_move:
                    # I like to moveitmoveit
                    new_agent_array[dest_i][dest_j] = new_agent_array[source_i][source_j]
                    self.array[dest_i][dest_j]=self.array[source_i][source_j]
                    new_agent_array[source_i][source_j] = None
                    # I like to moveitmoveit
                    self.array[source_i][source_j] = 0
                    # I like to MOVE IT
                    empty_locs[i] = source


        self.agent_array = deepcopy(new_agent_array)
        self.update_vis()
        return np.count_nonzero(self.array > 1)


    def update_vis(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.agent_array[i][j] is not None:
                    self.array[i][j] = deepcopy(self.agent_array[i][j].health) + 1

        # track numbers for each step
        self.healthy.append(np.count_nonzero(self.array == 1))
        self.contagious.append(np.count_nonzero((self.array > 1) & (self.array < 2)))
        self.sick.append(np.count_nonzero(self.array == 2))
