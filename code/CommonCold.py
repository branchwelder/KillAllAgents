"""
Definition of the common cold and how it affects agents.
"""

from random import randint

class CommonCold(Disease):
	def __init__(self, agent=None):
		"""
		Common attributes: strength, incubation
		Individual attributes: location, agent
		"""

		self.strength = 0.2 # Likelihood of infecting agents on contact 
		self.incubation = 60 # Average number of hours before agent is sick (2.5 days)
		self.duration = randint(48, 168) # Determines how many hours agents are sick

		super(CommonCold, self).__init__(agent, self.strength)

	def symptoms():
		"""
		Alters agent motion and attributes.
		"""
		pass

	def infect():
		"""
		Governs how the disease spreads between agents.
		"""
		pass