from abc import ABC
from uuid import uuid4, UUID

class BaseEntity(ABC):  
    def __init__(self, id: UUID = None):
      self.id = id or uuid4()
