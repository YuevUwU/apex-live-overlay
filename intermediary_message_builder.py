"""
Generate intermediary message such as Player.
WARNING: Developer haven't played Apex Legend.
I just refer to Apex Legend Wiki (Fandom) and ndekopen/liveapi_playgrounds
"""

import random
import string
import time

import names

from data import CHARACTERS, PLATFORMS, WEAPONS
from events_pb2 import Player, Vector3


def timestamp():
    return int(time.time())


def random_player():
    max_health = 100 # TODO
    shield_max_health = 25 * random.randint(0, 5)
    return Player(
        name=names.get_full_name(),
        teamId=random.randint(1, 20),
        pos=random_pos(),
        angles=random_angles(),
        maxHealth=max_health,
        currentHealth=random.randint(0, max_health),
        shieldMaxHealth=shield_max_health,
        shieldHealth=random.randint(0, shield_max_health),
        nucleusHash="".join([random.choice("0123456789abcdefg") for _ in range(128)]),
        hardwareName=random.choice(PLATFORMS),
        teamName="".join([random.choice(string.ascii_uppercase) for _ in range(3)]),
        squadIndex=random.randint(1, 3),
        character=random.choice(CHARACTERS),
        skin="skin",  # TODO
    )


def random_pos():
    return random_vector3(50000)


def random_angles():
    return random_vector3(180)


def random_vector3(abs_max):
    return Vector3(
        x=random.randint(-abs_max, abs_max),
        y=random.randint(-abs_max, abs_max),
        z=random.randint(-abs_max, abs_max),
    )
