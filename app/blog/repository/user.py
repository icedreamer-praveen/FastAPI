
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas
from blog.hashing import Hash


def create(request: schemas.User, db: Session):
    """
    This function creates a new user in the database with the provided name, email, and password.
    
    :param request: schemas.User - This is a Pydantic model that defines the structure of the incoming
    request data. It specifies the expected data types and formats for the user's name, email, and
    password
    :type request: schemas.User
    :param db: The "db" parameter is a database session object that is used to interact with the
    database. It is typically created using a database connection and provides methods for querying,
    inserting, updating, and deleting data from the database. In this case, it is being used to add a
    new user to the database
    :type db: Session
    :return: a newly created user object that has been added to the database after being hashed with
    bcrypt.
    """
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    """
    The function retrieves a user from a database based on their ID and returns it, or raises an
    HTTPException if the user is not found.
    
    :param id: The id parameter is an integer that represents the unique identifier of a user in the
    database
    :type id: int
    :param db: The "db" parameter is a SQLAlchemy session object that is used to interact with the
    database. It allows the function to query the database and retrieve the user with the specified ID
    :type db: Session
    :return: a user object from the database with the specified id. If the user is not found, it raises
    an HTTPException with a 404 status code and a message indicating that the user is not available.
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user