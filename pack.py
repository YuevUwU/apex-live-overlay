# pylint: disable=C0114,C0115,C0116
from events_pb2 import LiveAPIEvent
from google.protobuf import any_pb2

def pack(event):
    any_msg = any_pb2.Any()
    any_msg.Pack(event)

    live_api_event = LiveAPIEvent()
    live_api_event.event_size = event.ByteSize()
    live_api_event.gameMessage.CopyFrom(any_msg)

    message = live_api_event.SerializeToString()

    return message
