import os

import falu

falu.api_key = os.environ.get('FALU_API_KEY')

print("Getting messages: ...")

messages = falu.Messages.get_messages()

print("Messages retrieved: %r" % len(messages))

print("Sending message: ...")

sent_message = falu.Messages.send_message(
    data={'to': '+255715681850', 'stream': 'mstr_602ce49cc74dad6a38f99c2d', 'body': 'test'})

print("Message Sent: %r" % sent_message.id)

print("Getting message: ...")

message = falu.Messages.get_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print("Message retrieved: %r" % message.body)

print("Updating message: ...")

message = falu.Messages.update_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print("Message updated: %r" % message)

print("Canceling message: ...")

message = falu.Messages.cancel_message(message_id='msg_2mONJ2DZEVRy6jrfP8HUhemd8PJ')

print("Message canceled: %r" % message)
