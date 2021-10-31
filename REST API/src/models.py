from sqlalchemy import Column, Integer, String
from .database import Base


class Profile(Base):
    """
    Stores the profile data in the local database.
    """
    __tablename__ = "profiles"

    # unique Id stored as Integer for each profile
    id = Column(Integer, primary_key=True, index=True)

    # timestamp added in the form "%Y-%m-%d" "%H:%M:%S"
    # date = Column(Date, default=datetime.now().strftime("%Y-%m-%d" "%H:%M:%S"))

    # name is a string of max 50 characters which can't be null and its indexing is done.
    name = Column(String(50), nullable=False, index=True)

    # dob is also stored as string of length 10 and its indexing is also done.
    dob = Column(String(10), index=True)

    # status is stored as String which can accept value either ACTIVE or PAUSED.
    status = Column(String(6), index=True)
    