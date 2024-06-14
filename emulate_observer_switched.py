# pylint: disable=C0114,C0115,C0116
import asyncio
import random
import time

import websockets

from events_pb2 import ObserverSwitched
from intermediary_message_builder import random_player, timestamp
from pack import pack


async def send_message():
    uri = "ws://localhost:7777"
    async with websockets.connect(uri) as websocket:
        event = ObserverSwitched()

        event.timestamp = timestamp()
        event.category = "observer_switched"
        event.observer.CopyFrom(random_player())
        event.target.CopyFrom(random_player())
        event.targetTeam.extend([event.target, random_player(), random_player()])

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
