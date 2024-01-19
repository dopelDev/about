import uuid
from datetime import datetime, timedelta
import redis

class TemporalUUIDGenerator():
    def __init__(self):
        self.uuids = {}
        self.redis_vault = redis.Redis(host='localhost', port=6379, db=0)

    def generate_uuid(self, lifespan_minutes):
        new_uuid = str(uuid.uuid4())
        expiration_time = datetime.now() + timedelta(minutes=lifespan_minutes)
        self.uuids[new_uuid] = expiration_time
        self.redis_vault.set('uuids', new_uuid)
        return new_uuid
    
    def get_uuids(self):
        return self.uuids
