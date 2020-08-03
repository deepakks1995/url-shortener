from sqlalchemy import Column, String

from sqlalchemy.ext.declarative import declarative_base


class AvailableKeys(declarative_base()):
    """
    Available Keys Entity
    """
    __tablename__ = 'available_keys'
    keys = Column(String, primary_key=True)

    def __init__(self, keys) -> None:
        super().__init__()
        self.keys = keys




