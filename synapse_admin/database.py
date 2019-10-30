import psycopg2
from synapse_admin.config import config


query_levels = """
select
to_timestamp(origin_server_ts/1000) ts,
sender
, json::json->>'type' "type"
, json::json->'content' "content"
from events e
join event_json as ej using (event_id)
where
e.room_id = %s
and json::json->>'type' = 'm.room.power_levels'
order by origin_server_ts asc
"""

tezos_roomid = "!KNlqwBRiVdbAwkVpKO:matrix.org"
tezostrader_roomid = "!TUYwzSQkeKBLZlWldJ:matrix.org"


def get_level_events(roomid):
    conn = None
    rows = []
    try:
        params = config()
        conn = psycopg2.connect(**params)
        print(f"conn = {conn}")
        cur = conn.cursor()

        cur.execute(query_levels, (roomid,))
        rows = cur.fetchall()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return rows


