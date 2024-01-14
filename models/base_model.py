from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Parent class BaseModel"""

    def __init__(self, *args, **kwargs):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(value, date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(value, date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update current datetime (this is where you'd save to file or database)"""
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

    def __repr__(self):
        return self.__str__()