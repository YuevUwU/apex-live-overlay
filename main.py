# pylint: disable=C0114,C0115,C0116
import asyncio

import websockets
from google.protobuf import symbol_database, any_pb2

# Generated by protoc
import events_pb2  # pylint: disable=W0401,W0614
from team_data import custom_team_name

APEX_WS_HOST = "localhost"
APEX_WS_PORT = 7777

HTML_WS_HOST = "localhost"
HTML_WS_PORT = 4567

connected_clients: set[websockets.WebSocketServerProtocol] = set()


async def update_team_name(ws: websockets.WebSocketServerProtocol):
    print("Connected!")

    async for message in ws:
        incoming = events_pb2.LiveAPIEvent()
        incoming.ParseFromString(message)
        game_message: any_pb2.Any = incoming.gameMessage  # pylint: disable=E1101
        result_type = game_message.TypeName()
        msg_result = symbol_database.Default().GetSymbol(result_type)()
        game_message.Unpack(msg_result)
        print(f"type: {result_type}")

        if isinstance(msg_result, events_pb2.ObserverSwitched):
            target_player: events_pb2.Player = msg_result.target
            team_id: int = target_player.teamId
            team_name = str(custom_team_name.get(team_id, f"Team {team_id}"))

            if connected_clients:
                send_results = await asyncio.gather(
                    *[client.send(team_name) for client in connected_clients]
                )
                print(f"Number of clients sent: {len(send_results)}")

            print(f"Observer switched to Team {team_id}: {team_name}")


async def handle_outgoing(websocket: websockets.WebSocketServerProtocol):
    print("Client connected to sender!")
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)


async def main():
    receive_server = websockets.serve(update_team_name, APEX_WS_HOST, APEX_WS_PORT)
    send_server = websockets.serve(handle_outgoing, HTML_WS_HOST, HTML_WS_PORT)

    await asyncio.gather(
        receive_server,
        send_server,
    )
    print(f"Receiving on {APEX_WS_HOST}:{APEX_WS_PORT}...")
    print(f"Sending on {HTML_WS_HOST}:{HTML_WS_PORT}...")
    await asyncio.Future()


asyncio.run(main())
