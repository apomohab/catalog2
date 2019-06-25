#start on 19-6-2019 2:PM

from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base =  declarative_base()

class Catalog(Base):

    __tablename__ = 'catalog'

    id    = Column(Integer, primary_key=True)
    name  = Column(String(250), nullable=False)


class Items(Base):

    __tablename__ = 'menuitem'

    id            = Column(Integer, primary_key=True)
    title         = Column(String(250), nullable = False)
    details   = Column(String(250))
    category      = Column(String(250))
    catalog_id = Column(Integer,ForeignKey('catalog.id'))
    catalog    = relationship(Catalog)

# serializable format
    @property
    def serialize(self):

        return {
            'title': self.title,
            'details': self.details,
            'id': self.id,
            'category': self.category,
}

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
