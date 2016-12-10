from MovingWorld import MovingWorld
from WorldViewer import WorldViewer

from scipy.interpolate import interp1d

import matplotlib.pyplot as plt
import numpy as np
import thinkplot

def immunity_v_max(path, n, frames, num_agents, num_sick, moves_per_step):
    """Sweeps the moves_per_step parameter and creates a graph of the number
    of agents who are sick or contagious versus time for each immunity value.
    """
    maxes = []
    immunity_range = np.linspace(0.01, 1.0, num=100)
    for immunity in immunity_range:
        print(immunity)
        avg = []

        for run in range(5):
            grid = MovingWorld(n=n,
                               immunity=immunity,
                               num_agents=num_agents,
                               num_sick=num_sick,
                               moves_per_step=moves_per_step)

            # the World step method must return a value for this to work. In
            # this case, it returns the number that is sick or contagious.
            avg.append(max([grid.step() for i in range(frames)]))

        maxes.append(np.mean(avg))

    thinkplot.plot(immunity_range, maxes)

    thinkplot.config(xlabel='Immunity', ylabel='max sick',
                    loc='lower right')

    plt.savefig(path+'immunity_v_max_sweep.pdf')
    plt.clf()
    print("Immunity v. max sweep saved!")


def movement_v_max(path, n, frames, num_agents, num_sick, immunity):
    """Sweeps the moves_per_step parameter and creates a graph of the number
    of agents who are sick or contagious versus time for each immunity value.
    """
    maxes = []
    movement_range = np.linspace(0, 20, num=21)
    for movement in movement_range:
        print(movement)
        grid = MovingWorld(n=n,
                           immunity=immunity,
                           num_agents=num_agents,
                           num_sick=num_sick,
                           moves_per_step=int(movement))

        # the World step method must return a value for this to work. In
        # this case, it returns the number that is sick or contagious.

        maxes.append(max([grid.step() for i in range(frames)]))

    thinkplot.plot(movement_range, maxes)

    thinkplot.config(xlabel='Moves Per Step', ylabel='max sick',
                    loc='lower right', title="Number of Moves per Turn vs. Max Sick, num_agents=%d, n=%d" % (num_agents, n))

    plt.savefig(path+'movement_v_max_sweep.pdf')
    plt.clf()
    print("Immunity v. max sweep saved!")


def sweep_moves(path,
                n,
                frames,
                num_agents,
                num_sick,
                immunity):
    """Sweeps the moves_per_step parameter and creates a graph of the number
    of agents who are sick or contagious versus time for each immunity value.
    """
    for moves in np.linspace(0, 20, num=5):
        grid = MovingWorld(n=n,
                           immunity=immunity,
                           num_agents=num_agents,
                           num_sick=num_sick,
                           moves_per_step=int(moves))

        # the World step method must return a value for this to work. In this
        # case, it returns the number that is either sick or contagious.
        segs = [grid.step() for i in range(frames)]

        thinkplot.plot(segs, label='moves_per_step = %d' % moves)

    thinkplot.config(xlabel='Time steps', ylabel='num_sick + num_contagious',
                    loc='upper right', title="Sweeping Number of Moves per Turn, num_agents=%d, n=%d" % (num_agents, n))

    plt.savefig(path+'moves_per_step_sweep.pdf')
    plt.clf()
    print("Moves per step sweep saved!")

def sweep_immunity(path, n, frames, num_agents, num_sick, moves_per_step):
    """Sweeps the immunity parameter and creates a graph of the number of agents
    who are sick or contagious versus time for each immunity value.
    """
    for immunity in [0.1, 0.3, 0.5, 0.7, 0.8, 0.9]:
        grid = MovingWorld(n=n,
                           immunity=immunity,
                           num_agents=num_agents,
                           num_sick=num_sick,
                           moves_per_step=moves_per_step)

        # the World step method must return a value for this to work. In this
        # case, it returns the number that is either sick or contagious.
        segs = [grid.step() for i in range(frames)]

        thinkplot.plot(segs, label='immunity = %.2f' % immunity)

    thinkplot.config(xlabel='Time steps', ylabel='num_sick + num_contagious',
                    title='Sick Agents for Different Immunities, num_agents=%d, n=%d' % (num_agents, n), loc='upper right')

    plt.savefig(path+'immunity_sweep.pdf')
    plt.clf()
    print("Immunity sweep saved!")


def graph_bins(path,
               n,
               frames,
               num_agents,
               num_sick,
               moves_per_step,
               immunity):
    """Creates a graph of how many agents are in each bin (healthy, sick,
    contagious) over time.
    """

    world = MovingWorld(n=n,
                        num_agents=num_agents,
                        num_sick=num_sick,
                        moves_per_step=moves_per_step,
                        immunity=immunity)

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


def make_animation(path,
                   n,
                   frames,
                   fps,
                   num_agents,
                   num_sick,
                   moves_per_step,
                   immunity):
    """Makes an animation of World changing over "frames" steps.
    """

    world = MovingWorld(n=n,
                        num_agents=num_agents,
                        num_sick=num_sick,
                        moves_per_step=moves_per_step,
                        immunity=immunity)
    viewer = WorldViewer(world)

    # Create and save animation
    anim = viewer.animate(frames=frames)
    anim.save(path+"animation.mp4", fps=fps, extra_args=['-vcodec', 'libx264'])
    plt.clf()

    print("Animation saved!")

def run_experiment(path,
                   n,
                   frames,
                   fps,
                   num_agents,
                   num_sick,
                   moves_per_step,
                   immunity):
    """Runs the overall experiment. All output (animation and graphs) is saved
    to the output folder.
    """
    # make animation and save it
    make_animation(path, n, frames, fps, num_agents, num_sick, moves_per_step, immunity)

    # Make graphs

    # Shows change in number sick/contagious/healthy over time
    # graph_bins(path, n, frames, num_agents, num_sick, moves_per_step, immunity)

    # Sweeps immunity to show change
    # sweep_immunity(path, n, frames, num_agents, num_sick, moves_per_step)

    # Takes a very long time! Sweeps immunity and plots it versus the max number
    # of agents sick or contagious
    # immunity_v_max(path, n, frames, num_agents, num_sick, moves_per_step)

    # Sweeps the number of moves per step
    # sweep_moves(path, n, frames, num_agents, num_sick, immunity)
    # movement_v_max(path, n, frames, num_agents, num_sick, immunity)

    print("Experiment finished!")



if __name__ == "__main__":
    n = 30
    num_sick = 1
    moves_per_step = 3
    frames = 500
    fps = 10
    immunity = 0.7
    num_agents = int(n**2-(n**2/2))

    run_experiment("output/",
                   n=n,
                   frames=frames,
                   fps=fps,
                   num_agents=num_agents,
                   num_sick=num_sick,
                   moves_per_step=moves_per_step,
                   immunity=immunity)
