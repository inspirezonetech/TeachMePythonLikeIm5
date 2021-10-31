from typing import Optional
from datetime import date
from pydantic import BaseModel

# Base class with comman attributes
class ProfileBase(BaseModel):
    name: str
    dob: date
    status: Optional[str] = "ACTIVE"

# additional attributes while posting a Profile
class ProfileCreate(ProfileBase):
    # no additional attributes required.
    pass

# additional attributes in the database
class Profile(ProfileBase):
    # unique id to assigned to distinguish different profiles.
    id: int
    # we can also add the current timestamp with the below line.
    # created: datetime = datetime.now()

    class Config:
        orm_mode = True

# to return after posting a Profile
class ProfileId(BaseModel):
    id: int

    class Config:
        orm_mode = True

# to pause the profile status
class ProfilePause(BaseModel):
    status = "PAUSED"

    class Config:
        orm_mode = True

# to activate the profile status
class ProfileActivate(BaseModel):
    status = "ACTIVE"

    class Config:
        orm_mode = True
        