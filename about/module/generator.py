import uuid
import redis

class TemporalUUIDGenerator():
    def __init__(self):
        self.uuids = {}
        self.redis_vault = redis.Redis(host='localhost', port=6379, db=0)

    def generate_uuid(self, lifespan_minutes):
        new_uuid = str(uuid.uuid4())
        self.redis_vault.setex(new_uuid, lifespan_minutes * 60, 'active')
        return new_uuid
    
    def is_active(self, uuid):
        return self.redis_vault.exists(uuid)
