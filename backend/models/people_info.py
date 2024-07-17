from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PeopleInfo(Base):
    __tablename__ = 'people_info'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    job_title = Column(String)
    person_city = Column(String)
    person_state = Column(String)
    person_country = Column(String)
    email_pattern = Column(String)
    homepage_base_url = Column(String, ForeignKey('company_info.homepage_base_url'))
    duration_in_current_job = Column(String)
    duration_in_current_company = Column(String)
    email = Column(String)

    company = relationship("CompanyInfo", back_populates="employees")
