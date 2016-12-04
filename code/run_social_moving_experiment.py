from SocialMovingWorld import SocialMovingWorld
from WorldViewer import WorldViewer

import thinkplot
import matplotlib.pyplot as plt


def sweep_immunity(path, n, frames, num_agents, num_sick, moves_per_step):
    """Sweeps the immunity parameter and creates a graph of the number of agents
    who are sick or contagious versus time for each immunity value.
    """
    for immunity in [0.3, 0.6, 0.9]:
        grid = SocialMovingWorld(n=n,
                           immunity=immunity,
                           num_agents=num_agents,
                           num_sick=num_sick,
                           moves_per_step=moves_per_step)

        # the World step method must return a value for this to work. In this
        # case, it returns the number that is either sick or contagious.
        segs = [grid.step() for i in range(frames)]

        thinkplot.plot(segs, label='immunity = %.1f' % immunity)

    thinkplot.config(xlabel='Time steps', ylabel='num_sick + num_contagious',
                    loc='lower right')

    plt.savefig(path+'immunity_sweep.pdf')
    plt.clf()
    print("Immunity sweep saved!")


def graph_bins(path, n, frames, num_agents, num_sick, moves_per_step):
    """Creates a graph of how many agents are in each bin (healthy, sick,
    contagious) over time.
    """

    world = SocialMovingWorld(n=n,
                        num_agents=num_agents,
                        num_sick=num_sick,
                        moves_per_step=moves_per_step)

    for i in range(frames):
        world.step()

    thinkplot.plot(world.healthy, label='healthy')
    thinkplot.plot(world.sick, label='sick')
    thinkplot.plot(world.contagious, label='contagious')

    thinkplot.config(xlabel='Time steps', ylabel='num_agents',
                    loc='lower right')

    plt.savefig(path+'bin_graph.pdf')
    plt.clf()
    print("Bin graph saved!")


def make_animation(path, n, frames, fps, num_agents, num_sick, moves_per_step):
    """Makes an animation of World changing over "frames" steps.
    """

    world = SocialMovingWorld(n=n,
                        num_agents=num_agents,
                        num_sick=num_sick,
                        moves_per_step=moves_per_step)
    viewer = WorldViewer(world)

    # Create and save animation
    anim = viewer.animate(frames=frames)
    anim.save(path+"animation.mp4", fps=fps, extra_args=['-vcodec', 'libx264'])
    plt.clf()

    print("Animation saved!")

def run_experiment(path, n, frames, fps, num_agents, num_sick, moves_per_step):
    """Runs the overall experiment. All output (animation and graphs) is saved
    to the output folder.
    """
    # make animation and save it
    make_animation(path, n, frames, fps, num_agents, num_sick, moves_per_step)

    # Make graphs
    graph_bins(path, n, frames, num_agents, num_sick, moves_per_step)
    sweep_immunity(path, n, frames, num_agents, num_sick, moves_per_step)

    print("Experiment finished!")



if __name__ == "__main__":
    n = 20
    num_sick = 20
    moves_per_step = 3
    frames = 400
    fps = 7
    num_agents = n**2-100

    run_experiment("output/",
                   n=n,
                   frames=frames,
                   fps=fps,
                   num_agents=num_agents,
                   num_sick=num_sick,
                   moves_per_step=moves_per_step)
