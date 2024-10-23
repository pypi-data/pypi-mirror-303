import os
from typing import List
import numpy as np
import pygame
from itertools import product
from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Goal, Wall, Ball, WorldObj
from minigrid.minigrid_env import MiniGridEnv
from minigrid.wrappers import FullyObsWrapper
from gymnasium.core import ObservationWrapper
from knu_rl_env.grid_survivor.agent import GridSurvivorAgent


_MISSION_NAME = 'Grid Survivor!'
_BLUEPRINT_PATH = os.path.join(os.path.dirname(__file__), 'grid-survivor.csv')

_SYM_AGENT = 'A'
_SYM_START = 'S'
_SYM_GOAL = 'G'

_SYM_EMTPY = 'E'

_SYM_WALL = 'W'
_SYM_BALL = 'B'
_SYM_FOOD = 'F'
_SYM_BYSTANDER = 'B'
_SYM_OPPONENT = 'O'
_SYM_KILLER = 'K'

_DIR_RIGHT = 'R'
_DIR_DOWN = 'D'
_DIR_LEFT = 'L'
_DIR_UP = 'U'


_OBJ_ID_TO_SYM = {
    1: _SYM_EMTPY,
    2: _SYM_WALL,
    6: _SYM_BALL,
    8: _SYM_GOAL,
    10: _SYM_AGENT
}

_DIR_ID_TO_SYM = {
    0: _DIR_RIGHT,
    1: _DIR_DOWN,
    2: _DIR_LEFT,
    3: _DIR_UP
}

_COLOR_ID_RED = 0
_COLOR_ID_BLUE = 1
_COLOR_ID_GREEN = 2
_COLOR_ID_PURPLE = 3
_COLOR_ID_YELLOW = 4

DIR_TO_VEC = [
    np.array((-1, 0)),
    np.array((1, 0)),
    np.array((0, -1)),
    np.array((0, 1)),
]


class Bystander(Ball):
    def __init__(self):
        super().__init__(color='green')


class Food(Ball):
    def __init__(self):
        super().__init__(color='yellow')

    def can_overlap(self) -> bool:
        return True


class Opponent(Ball):
    def __init__(self):
        super().__init__(color='blue')

    def can_overlap(self) -> bool:
        return True


class Killer(Ball):
    def __init__(self):
        super().__init__(color='purple')

    def can_overlap(self) -> bool:
        return True


class GridSurvivorEnv(MiniGridEnv):
    def __init__(self, max_hit_points: int, max_steps: int, seed: int = None, **kwargs):
        blueprint = np.loadtxt(_BLUEPRINT_PATH, dtype=str, delimiter=',').T
        width, height = blueprint.shape
        start_pos = np.argwhere(blueprint == _SYM_START).flatten()
        assert len(start_pos) == 2, 'Only one start position should be provided.'

        goal_pos = np.argwhere(blueprint == _SYM_GOAL).flatten()
        assert len(goal_pos) == 2, 'Only one goal position should be provided.'

        self.blueprint = blueprint
        self.agent_start_pos = tuple(start_pos)
        self.agent_start_dir = 0
        self.goal_pos = tuple(goal_pos)

        self.bystanders = []
        self.opponents = []
        self.killers = []
        self.max_hit_points = self.hit_points = max_hit_points

        self.seed = seed
        self.rng = None

        super().__init__(
            mission_space=MissionSpace(self._gen_mission),
            width=width,
            height=height,
            max_steps=max_steps,
            **kwargs
        )

    @staticmethod
    def _gen_mission():
        return _MISSION_NAME

    def _gen_grid(self, width, height):
        self.grid = Grid(width, height)

        for x, y in product(range(width), range(height)):
            sym = self.blueprint[x, y]
            sym_key = sym[0] if len(sym) > 1 else sym

            if sym_key == _SYM_WALL:
                self.grid.set(x, y, Wall())
            elif sym_key == _SYM_BYSTANDER:
                obj = Bystander()
                self.put_obj(obj, x, y)
                self.bystanders.append(obj)
            elif sym_key == _SYM_OPPONENT:
                obj = Opponent()
                self.put_obj(obj, x, y)
                self.opponents.append(obj)
            elif sym_key == _SYM_FOOD:
                obj = Food()
                self.put_obj(obj, x, y)
            elif sym_key == _SYM_KILLER:
                obj = Killer()
                self.put_obj(obj, x, y)
                self.killers.append(obj)

        self.put_obj(Goal(), self.goal_pos[0], self.goal_pos[1])

        self.agent_pos = self.agent_start_pos
        self.agent_dir = self.agent_start_dir

    def _reward(self) -> float:
        return 0

    def _move_object_random(self, obj: WorldObj, max_tries: int):
        num_tries = 0
        ox, oy = obj.cur_pos
        positions = []

        for i in range(len(DIR_TO_VEC)):
            dx, dy = DIR_TO_VEC[i]
            nx, ny = ox + dx, oy + dy
            positions.append((nx, ny))

        while True:
            if num_tries > max_tries:
                raise RecursionError("rejection sampling failed in place_obj")
            num_tries += 1

            pos = self.rng.choice(positions)

            if self.grid.get(*pos) is not None:
                continue

            if np.array_equal(pos, self.agent_pos):
                continue

            break

        self.grid.set(pos[0], pos[1], obj)
        self.grid.set(ox, oy, None)

        if obj is not None:
            obj.cur_pos = pos

    def _move_object_toward_agent(self, obj: WorldObj, max_tries: int):
        if np.array_equal(obj.cur_pos, self.front_pos):
            return

        num_tries = 0
        ox, oy = obj.cur_pos
        ax, ay = self.agent_pos
        positions = []
        distances = np.zeros(len(DIR_TO_VEC))

        for i in range(len(DIR_TO_VEC)):
            dx, dy = DIR_TO_VEC[i]
            nx, ny = ox + dx, oy + dy
            dist = np.sqrt(np.square(nx - ax) + np.square(ny - ay))
            positions.append((nx, ny))
            distances[i] = dist

        probs = np.ones(len(DIR_TO_VEC))

        if np.all(distances != 0):
            min_dist = np.min(distances)
            probs[distances == min_dist] = 3

        probs = probs / np.sum(probs)

        while True:
            if num_tries > max_tries:
                raise RecursionError("rejection sampling failed in place_obj")
            num_tries += 1

            pos = self.rng.choice(positions, p=probs)

            if self.grid.get(*pos) is not None:
                continue

            if np.array_equal(pos, self.agent_pos):
                continue

            break

        self.grid.set(pos[0], pos[1], obj)
        self.grid.set(ox, oy, None)

        if obj is not None:
            obj.cur_pos = pos

    def _move_objects(self, objects: List[WorldObj], is_random: bool):
        for i in range(len(objects)):
            try:
                if is_random and self.rng.random() < .8:
                    self._move_object_random(
                        objects[i], max_tries=100
                    )
                elif not is_random:
                    self._move_object_toward_agent(
                        objects[i], max_tries=100
                    )
            except Exception:
                pass

    def reset(self, **kwargs):
        self.hit_points = self.max_hit_points
        self.rng = np.random.default_rng(self.seed)
        self.killers.clear()
        self.opponents.clear()
        self.bystanders.clear()
        self.action_count = 0
        return super().reset(**kwargs)

    def step(self, action):
        is_game_over = False

        if action == GridSurvivorAgent.ACTION_FORWARD:
            self.action_count += 1
            self._move_objects(self.bystanders, is_random=True)
            self._move_objects(self.opponents, is_random=False)
            self._move_objects(self.killers, is_random=False)

            front_obj = self.grid.get(*self.front_pos)
            is_eaten = front_obj and front_obj.type == 'ball' and front_obj.color == 'yellow'
            is_attacked = front_obj and front_obj.type == 'ball' and front_obj.color == 'blue'
            is_killed = front_obj and front_obj.type == 'ball' and front_obj.color == 'purple'

            if is_eaten:
                self.grid.set(front_obj.cur_pos[0], front_obj.cur_pos[1], None)
                self.hit_points = min(self.max_hit_points, self.hit_points + 1)
            elif is_attacked:
                self.grid.set(front_obj.cur_pos[0], front_obj.cur_pos[1], None)
                self.opponents.remove(front_obj)
                self.hit_points = max(0, self.hit_points - 1)
                is_game_over = self.hit_points <= 0
            elif is_killed:
                is_game_over = True

        obs, reward, terminated, truncated, info = super().step(action)

        if is_game_over:
            return obs, reward, True, truncated, info
        else:
            return obs, reward, terminated, truncated, info

    def render(self):
        img = self.get_frame(self.highlight, self.tile_size, False)

        if self.render_mode == "human":
            img = np.transpose(img, axes=(1, 0, 2))
            if self.render_size is None:
                self.render_size = img.shape[:2]
            if self.window is None:
                pygame.init()
                pygame.display.init()
                self.window = pygame.display.set_mode(
                    (self.screen_size, self.screen_size)
                )
                pygame.display.set_caption(_MISSION_NAME)
            if self.clock is None:
                self.clock = pygame.time.Clock()
            surf = pygame.surfarray.make_surface(img)

            # Create background with mission description
            offset = surf.get_size()[0] * 0.1
            # offset = 32 if self.agent_pov else 64
            bg = pygame.Surface(
                (int(surf.get_size()[0] + offset), int(surf.get_size()[1] + offset))
            )
            bg.convert()
            bg.fill((255, 255, 255))
            bg.blit(surf, (offset / 2, 0))

            bg = pygame.transform.smoothscale(bg, (self.screen_size, self.screen_size))
            font_size = 22
            distance = abs(self.agent_pos[0] - self.goal_pos[0]) + abs(self.agent_pos[1] - self.goal_pos[1])
            text = f'# Actions: {self.step_count}/{self.max_steps}; Distance: {distance}; HP: {self.hit_points}'
            font = pygame.freetype.SysFont(pygame.font.get_default_font(), font_size)
            text_rect = font.get_rect(text, size=font_size)
            text_rect.center = bg.get_rect().center
            text_rect.y = bg.get_height() - font_size * 1.5
            font.render_to(bg, text_rect, text, size=font_size)

            self.window.blit(bg, (0, 0))
            pygame.event.pump()
            self.clock.tick(5)
            pygame.display.flip()

        elif self.render_mode == "rgb_array":
            return img


class SymbolicObsWrapper(ObservationWrapper):
    def __init__(self, env):
        env = FullyObsWrapper(env)
        super().__init__(env)

    def observation(self, obs):
        obs = obs['image']
        width, height, _ = obs.shape
        grid = np.zeros((width, height)).astype('U3')
        for x, y in product(range(width), range(height)):
            obj, color, state = obs[x, y]
            obj = _OBJ_ID_TO_SYM.get(obj, _SYM_EMTPY)
            sym = obj
            if obj == _SYM_BALL:
                if color == _COLOR_ID_GREEN:
                    sym = _SYM_BYSTANDER
                elif color == _COLOR_ID_YELLOW:
                    sym = _SYM_FOOD
                elif color == _COLOR_ID_BLUE:
                    sym = _SYM_OPPONENT
                elif color == _COLOR_ID_PURPLE:
                    sym = _SYM_KILLER
            elif obj == _SYM_AGENT:
                state = _DIR_ID_TO_SYM.get(state)
                sym = f'{obj}{state}'

            grid[y, x] = sym
        return grid