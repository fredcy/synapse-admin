==============
Synapse-Admin
==============

This provides a report on Synapse admin events that change user power levels in a particular room.

------------
Install
------------

::

 poetry install


-------------
Configure
-------------

Set up a ``database.ini`` file at the root level with contents like this:
::

 [postgresql]
 host=localhost
 port=5433
 database=synapse
 user=synapse_reader
 password=foobarblah

This example assumes that postgres is configured with a user/role named ``synapse_reader``
that can login and query most synapse database tables.

---
Run
---
::

  poetry run python
  import synapse_admin.database
  import synapse_admin.report
  events = synapse_admin.database.get_level_events(synapse_admin.database.tezostrader_roomid)
  synapse_admin.report.report_admin_events(events)
 
