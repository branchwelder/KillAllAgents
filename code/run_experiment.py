from World import World
from WorldViewer import WorldViewer

import thinkplot
import matplotlib.pyplot as plt


def sweep_immunity(path, n, frames):
    for immunity in [0.3, 0.5, 0.8, 0.99]:
        grid = World(n=n, immunity=immunity)
        segs = [grid.step() for i in range(frames)]
        thinkplot.plot(segs, label='immunity = %.1f' % immunity)

    thinkplot.config(xlabel='Time steps', ylabel='num_sick + num_contagious',
                    loc='lower right')

    plt.savefig(path+'immunity_sweep.pdf')
    plt.clf()
    print("Immunity sweep saved!")


def graph_bins(path, n, frames):
    world = World(n=n)

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


def run_experiment(path, n, frames, fps):
    world = World(n=n)
    viewer = WorldViewer(world)

    # Create and save animation
    anim = viewer.animate(frames=frames)
    anim.save(path+"animation.mp4", fps=fps, extra_args=['-vcodec', 'libx264'])
    plt.clf()
    print("Animation saved!")

    # Make graphs`
    graph_bins(path, n, frames)
    sweep_immunity(path, n, frames)



if __name__ == "__main__":
    run_experiment("output/", n=100, frames=200, fps=5)
