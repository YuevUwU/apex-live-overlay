import asyncio

import websockets

# Generated by protoc
from events_pb2 import ObserverSwitched, Player
from team_data import custom_team_name

WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 7777

with open('templates/index.html', 'r') as f:
    html_template = f.read()

def generate_html(rank="", team_name="", score=""):
    return html_template.replace("{{ rank }}", rank) \
                        .replace("{{ team_name }}", team_name) \
                        .replace("{{ score }}", score)

async def modify_html(team_name: str):
    with open("index.html", 'w') as f:
        code = generate_html(team_name=team_name)
        f.write(code)

async def update_team_name(websocket):
    print("Connected!")

    async for message in websocket:
        # try:
        incoming = ObserverSwitched()
        incoming.ParseFromString(message)

        target_player: Player = incoming.target
        team_id: int = target_player.teamId
        team_name = str(custom_team_name.get(team_id, "Unknown"))

        await modify_html(team_name)
        print(f"Observer switched to Team {team_id}: {team_name}")

        # except Exception as e:
        #     print(message)
        #     print(e)


async def main():
    async with websockets.serve(update_team_name, WEBSOCKET_HOST, WEBSOCKET_PORT):
        print(f"Serving on {WEBSOCKET_HOST}:{WEBSOCKET_PORT}...")
        await asyncio.Future()


asyncio.run(main())