from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CompanyInfo(Base):
    __tablename__ = 'company_info'
    id = Column(Integer, primary_key=True)
    company_logo_url = Column(String)
    company_logo_text = Column(String)
    company_name = Column(String)
    relation_to_event = Column(String)
    event_url = Column(String, ForeignKey('event_info.event_url'))
    company_revenue = Column(Integer)
    n_employees = Column(Integer)
    company_phone = Column(String)
    company_founding_year = Column(String)
    company_address = Column(String)
    company_industry = Column(String)
    company_overview = Column(String)
    homepage_url = Column(String)
    linkedin_company_url = Column(String)
    homepage_base_url = Column(String)
    company_logo_url_on_event_page = Column(String)
    company_logo_match_flag = Column(String)

    event = relationship("EventInfo", back_populates="companies")
    employees = relationship("PeopleInfo", back_populates="company")
