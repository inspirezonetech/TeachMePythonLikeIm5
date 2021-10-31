from sqlalchemy.orm import Session
from typing import Optional
from . import models, schemas

# to get profile by id.
def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()


# to check if the same profile exist in the database
def get_same_profile(db: Session, name: str, dob: str, status: str):
    return db.query(models.Profile).filter(models.Profile.name == name, models.Profile.dob == dob, models.Profile.status == status).first()


# to get all the profiles...
def get_profiles(db: Session):
    return db.query(models.Profile).all()

# to get all paused profiles
def get_paused_profiles(db: Session):
    return db.query(models.Profile).filter(models.Profile.status == "PAUSED").all()


# to post a profile on the database.
def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


# to swap the status of profile
def update_status(db: Session, db_profile):
    # Update model class variable from requested fields
    if db_profile.status == "ACTIVE":
        update = schemas.ProfilePause()
    else:
        update = schemas.ProfileActivate()
    for var, value in vars(update).items():
        setattr(db_profile, var, value) if value else None
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


# to delete a profile
def delete_profile(db: Session, db_profile):
    db.delete(db_profile)
    db.commit()
    return {"message": "Profile successfully deleted!"}