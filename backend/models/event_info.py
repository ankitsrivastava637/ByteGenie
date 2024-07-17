from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class EventInfo(Base):
    __tablename__ = 'event_info'
    id = Column(Integer, primary_key=True)
    event_logo_url = Column(String)
    event_name = Column(String)
    event_start_date = Column(DateTime)
    event_end_date = Column(DateTime)
    event_venue = Column(String)
    event_country = Column(String)
    event_description = Column(String)
    event_url = Column(String)

    companies = relationship("CompanyInfo", back_populates="event")
