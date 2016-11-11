"""
World for sick and healthy agents
"""

import numpy as np
import random
from Cell2D import Cell2D

class World(Cell2D):

	def __init__(self, params, agent_array=None):

		# Set up world params
		self.dim = params.get("n", 0)
		self.num_population = params.get("num_agents", self.dim^2)
		self.num_sick = params.get("num_sick")

		# Set up the agent population
		if agent_array == None:
			# populate agent_array somehow
			self.agent_array = None
		else:
			self.agent_array = agent_array

		# Set up occupancy grid to keep track of agent presence
		self.occupancy_grid = np.zeros(n, n)
		for x in range(0, n-1):
			for y in range(0, n-1): 
				if self.agent_array[i][j] != None:
					self.occupancy_grid[i][j] = 1

		# Create an agent health visualization array
		self.array = np.zeros(n, n)


	# Every step represents the change in one hour
	def step(self):

		# Loop through agent objects and update based on params
		for i in range(0, n-1):
			for j in range(0, n-1):
				if agent_array[i][j] != None:
					# Get list of neighbors health
					neighbors_health = []
					for a in range(i - 1, i + 2):
						for b in range(j - 1, j + 2):
							if (a, b) != (i, j):
								neighbors_health.append(agent_array[a][b].health)

					# Get fraction of neighbors that are sick
					np.ceil(neighbors_health)
					neigh_health_frac = sum(neighbors_health) / len(neighbors_health)

					# Update agent health
					# If sick (and contagious)
					if agent_array[i][j].health == 1:
						if random.randrange(0, 100) == 1:
							agent_array[i][j].health = 0

					# If health and contagious
					elif agent_array[i][j].health < 1 and agent_array[i][j].health > 0:
						agent_array[i][j].health += 0.1	

					# If healthy
					else:
						if random.randrange(neigh_health_frac*100, 100) > agent_array[i][j].immunity*100:
							agent_array[i][j].health = 0.1

		udate_vis(self.agent_array)


	def update_vis(self, agents):
		for i in range(0, n-1):
			for j in range(0, n-1):
				self.array[i][j] = self.agent[i][j].health + 1