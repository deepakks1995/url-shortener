from sqlalchemy import Column, String

from sqlalchemy.ext.declarative import declarative_base


class URL(declarative_base()):
    """
    URL Entity
    """
    __tablename__ = 'url'
    custom = Column(String, primary_key=True)
    original = Column(String)

    def __init__(self, hash, orig) -> None:
        super().__init__()
        self.custom = hash
        self.original = orig


