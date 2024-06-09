import asyncio
import random
import time

import websockets

from events_pb2 import ObserverSwitched, Player, Vector3


async def send_message():
    uri = "ws://localhost:7777"
    async with websockets.connect(uri) as websocket:
        now = int(time.time())
        event = ObserverSwitched()

        event.timestamp: int = now
        event.category: str = "observer_switched"
        pos_template = Vector3(x=1328.387999, y=1827.918209, z=28798.222121)
        angles_template = Vector3(x=13.387999, y=18.918209, z=287.222121)
        player_template = Player(
            name="sampleuser",
            teamId=random.randint(0, 21),
            pos=pos_template,
            angles=angles_template,
            currentHealth=80,
            maxHealth=100,
            shieldHealth=23,
            shieldMaxHealth=50,
            nucleusHash="aece34233800286dce1058e7d93d17a4f9fbbd1443f49a0d6326cabe33a4346d091ba6efb20f4d3cbbe1289c675b266c5bc16dc12a8948d9c1f456b728312536",
            hardwareName="PS4",
            teamName="Team1's Name",
            squadIndex=1,
            character="Valkyrie",
            skin="Military Grade",
        )
        event.observer.CopyFrom(player_template)
        event.observer.name = "observer"
        event.target.CopyFrom(player_template)
        event.target.name = "target"
        event.targetTeam.add()

        message = event.SerializeToString()

        await websocket.send(message)
        # print(message)
        print("Message sent")


while True:
    try:
        asyncio.run(send_message())
    except ConnectionRefusedError:
        print("Connect call failed")
    time.sleep(random.randint(200, 3000) / 1000)
