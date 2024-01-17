import uuid
import time
from datetime import datetime, timedelta

class TemporalUUIDGenerator(object):
    def __init__(self, node_id):
        self.uuids = {}

    def generator_uuid(self, lifespan_minutes):
        new_uuid = str(uuid.uuid4())
        expiration_time = datetime.now() + timedelta(minutes=lifespan_minutes)
        self.uuids[new_uuid] = expiration_time
        return new_uuid
    
    def cleanup_uuids(self):
        current_time = datetime.now()
        expired_uuids = [uuid for uuid, expiration_time in self.uuids.items() if expiration_time < current_time]
        for uuid in expired_uuids:
            del self.uuids[uuid]

    def get_uuids(self):
        return self.uuids
