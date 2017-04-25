"""
Lambda Handler to send message to somebody
"""

import fbchat

from secret_settings import MY_PASSWORD, MY_UID

def send_message(target_list, message):
    """
    @param target: list of friend_uids to send messages to
    """
    client = fbchat.Client(MY_UID, MY_PASSWORD)
    for target in target_list:
        client.send(target, message)
