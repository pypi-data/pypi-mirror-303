import pygame
from minigrid.manual_control import ManualControl
from .agent import GridSurvivorAgent
from .env import GridSurvivorEnv, SymbolicObsWrapper


def _make_grid_survivor(show_screen: bool, with_wrapper: bool):
    env = GridSurvivorEnv(
        render_mode='human' if show_screen else 'rgb_array',
        max_hit_points=15,
        max_steps=2000,
        seed=None
    )
    if with_wrapper:
        env = SymbolicObsWrapper(env)

    return env


def make_grid_survivor(show_screen: bool):
    return _make_grid_survivor(show_screen, with_wrapper=True)


def evaluate(agent: GridSurvivorAgent):
    env = make_grid_survivor(show_screen=True)
    done = False
    observation, _ = env.reset()

    while not done:
        action = agent.act(observation)
        observation, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                env.close()
                break

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(int(event.key))
                if key == 'escape':
                    env.close()
                    return


def run_manual():
    env = _make_grid_survivor(show_screen=True, with_wrapper=False)
    env = ManualControl(env)
    env.start()
