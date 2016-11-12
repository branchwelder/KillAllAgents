from World import World
from WorldViewer import WorldViewer


def make_animation(path, frames, fps):
    world = World()
    viewer = WorldViewer(world)
    anim = viewer.animate(frames=frames)

    anim.save(path, fps=fps, extra_args=['-vcodec', 'libx264'])


if __name__ == "__main__":
    make_animation("output/basic_animation.mp4", 100, 5)
