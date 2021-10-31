from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
# intialising the app
app = FastAPI(title="REST API", docs_url="/", redoc_url="/doc")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Database Dependency
def get_db():
    db = SessionLocal()
    # trying to yield the database
    try:
        yield db
    finally:
        db.close()


@app.post("/profiles", tags=["Create Profile"], response_model=schemas.ProfileId)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    """
    Create Profile add it in the database.

    Args:
        profile (schemas.ProfileCreate): The data to be added.
        db (Session, optional): The database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 409.

    Returns:
        id: create profile and returns the unique id.
    """
    db_profile = crud.get_same_profile(db, name=profile.name, dob=profile.dob, status=profile.status)
    # if profile already exists in the database.
    if db_profile:
        raise HTTPException(status_code=409, detail="Profile already exists")
    return crud.create_profile(db=db, profile=profile)


@app.get("/profiles", tags=["View Profile"], response_model=List[schemas.Profile])
def read_profiles(db: Session = Depends(get_db)):
    """
    View all the profile in the database.

    Args:
        db (Session, optional): The database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 404.

    Returns:
        json: Return all profiles.
    """
    db_profiles = crud.get_profiles(db)
    # if no profile is returned.
    if db_profiles is None:
        raise HTTPException(status_code=404, detail="No profiles exist!")
    return db_profiles


@app.get("/profiles/{profile_id}", tags=["View Profile"], response_model=schemas.Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    View profile with having the given Id.

    Args:
        profile_id (int): The unique Id of the profile.
        db (Session, optional): The database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 404.

    Returns:
        json: Return the profile with given Id.
    """
    db_profile = crud.get_profile(db, profile_id=profile_id)
    # if no profile is returned.
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Id doesn’t exist!")
    return db_profile


@app.get("/paused_profiles", tags=["View Profile"], response_model=List[schemas.Profile])
def read_paused_profiles(db: Session = Depends(get_db)):
    """
    Return all profiles with status = "PAUSED".

    Args:
        db (Session, optional): The Database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 404.

    Returns:
        json: Return all profiles with status = "PAUSED".
    """
    db_profiles = crud.get_paused_profiles(db)
    # if no profile is returned.
    if db_profiles is None:
        raise HTTPException(status_code=404, detail="No profiles exist!")
    return db_profiles


@app.patch("/profiles/{profile_id}", tags=["Update Status"])
def update_status(profile_id: int, db: Session = Depends(get_db)):
    """
    Swap the status of the profile with given Id.

    Args:
        profile_id (int): the unique profile Id.
        db (Session, optional): The database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 404.

    Returns:
        profile: the profile object with updated status.
    """
    # getting the existing data
    db_profile = crud.get_profile(db, profile_id=profile_id)
    # if no profile is returned.
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Id doesn’t exist!")
    return crud.update_status(db=db, db_profile=db_profile)


@app.delete("/profiles/{profile_id}", tags=["Delete Profile"])
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    Delete the profile with given profile Id.

    Args:
        profile_id (int): the unique profile Id.
        db (Session, optional): The database. Defaults to Depends(get_db).

    Raises:
        HTTPException: The HTTP Exception with status code 404.

    Returns:
        message: "Profile successfully deleted!"
    """
    # getting the existing data
    db_profile = crud.get_profile(db, profile_id=profile_id)
    # if no profile is returned.
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Id doesn’t exist!")
    return crud.delete_profile(db=db, db_profile=db_profile)
