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

    return dist_arr

if __name__ == "__main__":
    print(city_init(num_agents=10,n=5))
