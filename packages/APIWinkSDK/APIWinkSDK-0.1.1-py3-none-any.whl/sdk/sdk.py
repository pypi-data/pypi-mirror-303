import hashlib

class SDK:
    def __init__(self, walletid, serviceid, reqs) -> None:
        self.walletid = walletid
        self.serviceid = serviceid
        self.reqs = reqs
        self.api_key = self.generate_api_key()
    
    def generate_api_key(self):
        key_string = f"{self.walletid}:{self.serviceid}"
        return hashlib.sha256(key_string.encode()).hexdigest()

    def validate(self):
        if self.reqs > 0:
            self.reqs -= 1
            return True
        return False
    
    def refill(self, num_reqs):
        self.reqs = num_reqs
        return True

class APIKeyManager:
    def __init__(self):
        self.instances = {}

    def create_key(self, walletid, serviceid, reqs):
        sdk = SDK(walletid, serviceid, reqs)
        self.instances[sdk.api_key] = sdk
        return sdk.api_key

    def validate_request(self, api_key):
        if api_key in self.instances:
            return self.instances[api_key].validate()
        return False
    
    def add_refills(self, api_key, num_requests):
        if api_key in self.instances:
            return self.instances[api_key].refill(num_requests)
        return False
