from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import database, schemas
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    """
    This function creates a user in the database using the provided user data and returns the created
    user.
    
    :param request: The request parameter is an instance of the User schema, which is used to represent
    the data that is being sent in the request body when creating a new user. It contains attributes
    such as username, email, and password
    :type request: schemas.User
    :param db: The parameter `db` is a database session object that is created using the `get_db`
    function. It is used to interact with the database and perform CRUD (Create, Read, Update, Delete)
    operations on the user data. The `Depends` function is used to inject the database session
    :type db: Session
    :return: The function `create_user` is returning the result of calling the `create` function from
    the `user` module with the `request` object and the `db` object as arguments. The specific return
    value depends on the implementation of the `create` function.
    """
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    """
    This function retrieves a user with a specific ID from a database.
    
    :param id: id is an integer parameter that represents the unique identifier of a user. It is used to
    retrieve information about a specific user from the database
    :type id: int
    :param db: The parameter `db` is a dependency injection that is used to obtain a database session.
    It is of type `Session`, which is a SQLAlchemy session object that allows us to interact with the
    database. The `Depends` function is used to declare the dependency on the `get_db` function,
    :type db: Session
    :return: The function `get_user` returns the result of calling the `show` function from the `user`
    module with the `id` parameter and the `db` parameter obtained from the `get_db` function. The
    specific return value depends on the implementation of the `show` function.
    """
    return user.show(id, db)