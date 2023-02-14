#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    '''' this is a BaseModel class for creating air-bnb users'''

    def __init__(self, id=uuid.uuid4(), created_at=datetime.now(), updated_at=datetime.now()):
        # initalization of class attributes
        self.id = str(id)
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f' {self.__class__} {self.id} {self.__dict__}'

    def save(self):
        return self.updated_at

    def to_dict(self):
        return self.__dict__

