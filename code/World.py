"""
World for sick and healthy agents
"""

from Agent import Agent
import numpy as np
import random
from Cell2D import Cell2D

class World(Cell2D):

	def __init__(self, agent_array=None, **params):

		# Set up world params
		self.dim = params.get("n", 0)
		self.num_population = params.get("num_agents", self.dim**2)
		self.num_sick = params.get("num_sick", 0)

		# Set up the agent population
		if agent_array == None:
			# populate agent_array
			self.agent_array = [[None for x in range(self.dim)] for y in range(self.dim)]
			sick_list = [1 for _ in range(self.num_sick)]
			healthy_list = [0 for _ in range(self.dim**2 - self.num_sick)]
			health_shuffle = sick_list + healthy_list
			random.shuffle(health_shuffle)

			for i in range(self.dim):
				for j in range(self.dim):
					self.agent_array[i][j] = Agent(health=health_shuffle[self.dim * i + j])
		else:
			self.agent_array = agent_array

		# Set up occupancy grid to keep track of agent presence
		self.occupancy_grid = np.zeros((self.dim, self.dim))
		for x in range(self.dim-1):
			for y in range(self.dim-1): 
				if self.agent_array[i][j] != None:
					self.occupancy_grid[i][j] = 1

		# Create an agent health visualization array
		self.array = np.zeros((self.dim, self.dim))


	# Every step represents the change in one hour
	def step(self):

		# Loop through agent objects and update based on params
		for i in range(self.dim-1):
			for j in range(self.dim-1):
				if self.agent_array[i][j] != None:
					# Get list of neighbors health
					neighbors_health = []
					for a in range(i - 1, i + 2):
						for b in range(j - 1, j + 2):
							if (a, b) != (i, j):
								neighbors_health.append(self.agent_array[a][b].health)

					# Get fraction of neighbors that are sick
					np.ceil(neighbors_health)
					neigh_health_frac = sum(neighbors_health) / len(neighbors_health)

					# Update agent health
					# If sick (and contagious)
					if self.agent_array[i][j].health == 1:
						if random.randrange(0, 100) == 1:
							self.agent_array[i][j].health = 0

					# If health and contagious
					elif self.agent_array[i][j].health < 1 and self.agent_array[i][j].health > 0:
						self.agent_array[i][j].health += 0.1	

					# If healthy
					else:
						if random.randrange(int(neigh_health_frac*100), 100) > self.agent_array[i][j].immunity*100:
							self.agent_array[i][j].health = 0.1

		self.update_vis()


	def update_vis(self):
		for i in range(self.dim-1):
			for j in range(self.dim-1):
				self.array[i][j] = self.agent_array[i][j].health + 1