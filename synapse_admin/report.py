from synapse_admin.database import get_level_events
from pprint import (pprint, pformat)

def report_admin_events(events):
    levels = {}

    for event in events:
        (timestamp, sender, event_type, content) = event
        print(f"\n{timestamp}\t{sender}")
        #pprint(content['users'])

        users_to_del = []
        for user, level in levels.items():
            if user not in content['users']:
                print(f"{user}: {levels[user]} -> ?")
                users_to_del.append(user)

        for user in users_to_del:
                del levels[user]

        for user, level in content['users'].items():
            if user not in levels:
                print(f"{user}: ? -> {level}")
                levels[user] = level
            elif level != levels[user]:
                print(f"{user}: {levels[user]} -> {level}")
                levels[user] = level

