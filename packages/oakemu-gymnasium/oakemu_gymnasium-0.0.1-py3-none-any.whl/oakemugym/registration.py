from collections.abc import Sequence
from typing import NamedTuple

import gymnasium as gym


class EnvConfig(NamedTuple):
    version: str


def register_envs(games: Sequence[str], configs: Sequence[EnvConfig]):
    for game in games:
        for config in configs:
            gym.register(
                id=f"{game}-{config.version}",
                entry_point="oakemugym.oakemuenv:OakEmuEnv",
                kwargs=dict(
                    game_type=game,
                    obs_type="spectrum",
                ),
            )


def register():
    games = ["ManicMiner"]
    versions = [EnvConfig(version="v0")]

    register_envs(games, versions)
