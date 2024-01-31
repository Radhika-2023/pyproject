from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, REAL, ForeignKey


class Organizations(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Locations(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable=False)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

