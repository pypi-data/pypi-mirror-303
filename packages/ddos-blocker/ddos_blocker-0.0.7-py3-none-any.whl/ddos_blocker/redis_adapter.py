from datetime import datetime

import redis


class RedisAdapter:
    def __init__(
        self,
        host="localhost",
        port=6379, db=0, timeout=5 * 60,
        max_requests=100
    ):

        self.host = host
        self.port = port
        self.db = db
        self.timeout = timeout
        self.max_requests = int(max_requests)
        self.client = redis.StrictRedis(host=self.host,
                                        port=self.port,
                                        db=self.db)

        self.check_connection()

    def check_connection(self):
        try:
            self.client.ping()
        except redis.ConnectionError as e:
            print(f"Error connecting to Redis: {e}")
            raise

    def set_ip_mask(self, ip):
        """Sets the value for the IP address with timestamp."""
        key = f"{ip}:{datetime.now()}"
        self.client.setex(key, self.timeout, 1)

    def get_keys(self, ip):
        """Returns all keys that match the pattern for the given IP."""
        keys = self.client.keys(f"{ip}:*")
        return keys

    def count_keys(self, ip):
        """Counts the number of keys for a given IP."""
        return len(self.get_keys(ip))
