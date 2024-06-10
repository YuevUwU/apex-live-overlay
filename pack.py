from events_pb2 import *
from google.protobuf.any_pb2 import Any

def pack(event):
    any_msg = Any()
    any_msg.Pack(event)

    live_api_event = LiveAPIEvent()
    live_api_event.event_size = event.ByteSize()
    live_api_event.gameMessage.CopyFrom(any_msg)

    message = live_api_event.SerializeToString()

    return message
