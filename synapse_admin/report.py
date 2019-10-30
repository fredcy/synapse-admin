from synapse_admin.database import get_level_events
from pprint import pprint, pformat


def report_admin_events(events):
    """ Read a list of synapse admin events and report changes to user power levels.
    """
    levels = {}  # keeps track of user -> level mapping over time
    show_mutes = False

    for event in events:
        (timestamp, sender, event_type, content) = event
        print(f"\n{timestamp}\t{sender}")

        # report on users where the prior known level is gone
        users_to_del = []
        for user, level in sorted(levels.items(), key=lambda kv: kv[0].lower()):
            if user not in content["users"]:
                if level != -1 or show_mutes:
                    print(f"{user}: {level} -> ?")
                users_to_del.append(user)

        for user in users_to_del:
            del levels[user]

        # now report on users listed in current event
        for user, level in sorted(
            content["users"].items(), key=lambda kv: kv[0].lower()
        ):
            if user not in levels:
                if level != -1 or show_mutes:
                    print(f"{user}: ? -> {level}")
                levels[user] = level
            elif level != levels[user]:
                if level != -1 or show_mutes:
                    print(f"{user}: {levels[user]} -> {level}")
                levels[user] = level
