from pydantic import BaseModel

class DNSRecord(BaseModel):
    domain: str
    ip_address: str

    def __init__(self, data:list):
        super().__init__(domain=data[0], ip_address=data[1])