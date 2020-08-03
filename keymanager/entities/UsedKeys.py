from sqlalchemy import Column, String

from sqlalchemy.ext.declarative import declarative_base


class UsedKeys(declarative_base()):
    """
    Used Keys Entity
    """
    __tablename__ = 'used_keys'
    keys = Column(String, primary_key=True)

    def __init__(self, keys) -> None:
        super().__init__()
        self.keys = keys




