# pylint: disable=C0114,C0115,C0116
import asyncio
import random
import time

import websockets

from data import WEAPONS
from events_pb2 import PlayerKilled
from intermediary_message_builder import random_player, timestamp
from pack import pack


async def send_message():
    uri = "ws://localhost:7777"
    async with websockets.connect(uri) as websocket:
        event = PlayerKilled()

        event.timestamp = timestamp()
        event.category = "player_killed"
        event.attacker.CopyFrom(random_player())
        event.victim.CopyFrom(random_player())
        event.awardedTo.CopyFrom(random_player())
        event.weapon = random.choice(WEAPONS)

        message = pack(event)

        await websocket.send(message)
        # print(message)
        print("Message sent")


while True:
    try:
        asyncio.run(send_message())
    except ConnectionRefusedError:
        print("Connect call failed")
    time.sleep(random.randint(200, 3000) / 1000)
