from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import database, oauth2, schemas
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    This function returns all blog posts using the database session and the current authenticated user.
    
    :param db: The "db" parameter is a dependency injection of the database session object obtained from
    the "get_db" function. It is used to interact with the database and perform CRUD operations
    :type db: Session
    :param current_user: The parameter `current_user` is of type `schemas.User` and is obtained using
    the `Depends` function with the `oauth2.get_current_user` dependency. This means that it is
    expecting an authenticated user to be passed in as a parameter. The `get_current_user` function will
    check
    :type current_user: schemas.User
    :return: The function `all` returns the result of calling the `get_all` function from the `blog`
    module, passing in the `db` parameter. The `db` parameter is obtained by calling the `get_db`
    function, which returns a database session. The `current_user` parameter is obtained by calling the
    `get_current_user` function from the `oauth2` module, which returns
    """
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    This function creates a new blog post in the database with the provided request data and returns the
    created blog post.
    
    :param request: The request parameter is an instance of the Blog schema, which is used to represent
    the data that is being sent in the HTTP request body. It contains the information needed to create a
    new blog post, such as the title, content, and author
    :type request: schemas.Blog
    :param db: db is a parameter that represents the database session. It is of type Session, which is a
    class provided by SQLAlchemy that represents a connection to the database. The session is used to
    execute database queries and transactions. In this case, the session is obtained using the get_db
    function, which is a dependency
    :type db: Session
    :param current_user: The parameter `current_user` is of type `schemas.User` and is obtained using
    the `Depends` function with the `oauth2.get_current_user` dependency. This means that it is
    expecting an authenticated user to be passed in with the request, and it will retrieve the user
    information from the
    :type current_user: schemas.User
    :return: The `create` function is returning the result of calling the `create` function from the
    `blog` module with the `request` and `db` arguments. The specific return value depends on the
    implementation of the `create` function in the `blog` module.
    """
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    This function destroys a blog post with a given ID using the database session and the current
    authenticated user.
    
    :param id: The id parameter is an integer that represents the unique identifier of a blog post that
    needs to be deleted from the database
    :type id: int
    :param db: db is a parameter of type Session that is obtained by calling the get_db function using
    the Depends dependency injection. This parameter is used to access the database session and perform
    CRUD operations on the database. The Session object is provided by the SQLAlchemy ORM and represents
    a transactional scope for interacting with the database
    :type db: Session
    :param current_user: The "current_user" parameter is a dependency that is obtained using the
    "get_current_user" function from the "oauth2" module. This function is responsible for
    authenticating the user and returning their user information, which is then passed to the "destroy"
    function as a parameter of type "schemas
    :type current_user: schemas.User
    :return: The `destroy` function is returning the result of calling the `destroy` function from the
    `blog` module, passing in the `id` and `db` arguments. The specific return value of the `destroy`
    function depends on its implementation in the `blog` module.
    """
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    This function updates a blog post with the given ID using the information provided in the request,
    while also checking for authentication of the current user.
    
    :param id: The id parameter is an integer that represents the unique identifier of a blog post in
    the database. It is used to identify the specific blog post that needs to be updated
    :type id: int
    :param request: The `request` parameter is of type `schemas.Blog`, which is a Pydantic model
    representing the data that is being sent in the request body. It contains the updated information
    for a blog post that needs to be updated in the database
    :type request: schemas.Blog
    :param db: The "db" parameter is a dependency injection of the database session obtained from the
    "get_db" function. It is used to interact with the database and perform CRUD operations on the
    "Blog" model
    :type db: Session
    :param current_user: The current_user parameter is a dependency that uses the OAuth2 authentication
    system to get the current user making the request. It is of type schemas.User, which is a Pydantic
    model representing a user in the database. This parameter is used to ensure that only authenticated
    users can update a blog post
    :type current_user: schemas.User
    :return: The `update()` function is returning the result of calling the `blog.update()` function
    with the provided `id`, `request`, and `db` arguments. The specific return value of `blog.update()`
    is not shown in the provided code snippet.
    """
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    This function returns the result of calling the "show" function from the "blog" module with the
    provided "id", "db", and "current_user" arguments.
    
    :param id: The id parameter is of type int and represents the unique identifier of a blog post
    :type id: int
    :param db: The "db" parameter is a dependency injection that is used to get a database session
    object. It is passed to the function using the "Depends" function from the FastAPI framework. The
    "get_db" function is responsible for creating a new database session object and returning it. This
    session object
    :type db: Session
    :param current_user: The parameter `current_user` is of type `schemas.User` and is used as a
    dependency in the FastAPI application to get the current authenticated user. It is obtained using
    the `oauth2.get_current_user` function, which checks the authentication token in the request header
    and returns the user associated with
    :type current_user: schemas.User
    :return: the result of calling the `show` function from the `blog` module with the provided `id` and
    `db` arguments. The result of this function call is then returned by the `show` function in this
    code snippet.
    """
    return blog.show(id, db)