import numpy as np

def distance(x, y):
    """Helper function for initializing each cell in the array with
    a distance from the city center.
    """
    x_dist = abs(x-city_center)
    y_dist = abs(y-city_center)
    return np.sqrt(x_dist**2 + y_dist**2)


def city_init(num_agents=100, n=100, sick=0.01, contagious=0.04, healthy=0.45, empty=0.5):
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

    #empty is 0, sick is 1, contagious is 2, healthy is 3
    choices = [0, 1, 2, 3]
    probs = [empty, sick, contagious, healthy]

    # We'll have to change this to account for the city, but I can't do it
    # right now as the agent class isn't written yet
    # What we probably want to do is something like sugarscape, where we make
    # the agents first and then interate through them and place them
    # This is just a placeholder for now, so we have an output array of agent
    # positions.
    agent_array = np.random.choice(choices, (n, n), p=probs).astype(np.int8)

    return dist_arr, agent_array

if __name__ == "__main__":
    print(city_init(num_agents=10,n=5))
