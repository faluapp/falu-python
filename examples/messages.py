import os

import falu
from falu.client.json_patch_document import JsonPatchDocument

falu.api_key = os.environ.get('FALU_API_KEY')

print("Getting messages: ...")

messages, error = falu.Messages.get_messages()

if error is None:
    print("Messages retrieved: %r" % len(messages))
else:
    print(error.status_code)

print("Sending message: ...")

sent_message, error = falu.Messages.send_message(
    data={'to': '+255715681850', 'stream': 'mstr_602ce49cc74dad6a38f99c2d', 'body': 'test'})

print("Message Sent: %r" % sent_message.id)

print("Getting message: ...")

message, error = falu.Messages.get_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print("Message retrieved: %r" % message.body)

print("Updating message: ...")

message, error = falu.Messages.update_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ',
                                              document=JsonPatchDocument())

print("Message updated: %r" % message)

print("Canceling message: ...")

message, error = falu.Messages.cancel_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print("Message canceled: %r" % message)
