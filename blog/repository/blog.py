from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas


def get_all(db: Session):
    """
    The function retrieves all blogs from the database.
    
    :param db: Session
    :type db: Session
    :return: The function `get_all` returns a list of all the `Blog` objects in the database.
    """
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    """
    This function creates a new blog post in the database with the provided title, body, and user ID.
    
    :param request: schemas.Blog - This is a Pydantic model that defines the structure of the incoming
    request data. It specifies the expected data types and formats for the title and body of the blog
    post
    :type request: schemas.Blog
    :param db: Session is an instance of the SQLAlchemy Session class, which represents a transactional
    database connection. It is used to interact with the database and perform CRUD (Create, Read,
    Update, Delete) operations. In this case, the Session is used to add a new blog post to the
    database, commit the
    :type db: Session
    :return: a newly created blog post as an instance of the Blog model.
    """
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    """
    This function deletes a blog from the database based on its ID.
    
    :param id: The id parameter is an integer that represents the unique identifier of a blog post in
    the database
    :type id: int
    :param db: The "db" parameter is an instance of the SQLAlchemy Session class, which is used to
    interact with the database. It allows the function to query, insert, update, and delete data from
    the database. The Session class manages the transactional state of the database and provides a
    high-level interface for working
    :type db: Session
    :return: a string 'done' after deleting a blog with the given id from the database using the
    SQLAlchemy ORM. If the blog with the given id is not found, it raises an HTTPException with a 404
    status code and a message indicating that the blog was not found.
    """
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Blog, db: Session):
    """
    This function updates a blog post in the database with the given ID using the information provided
    in the request.
    
    :param id: The id parameter is an integer that represents the unique identifier of the blog that
    needs to be updated
    :type id: int
    :param request: The request parameter is an instance of the Blog schema, which is used to update the
    blog post with the given id in the database. It contains the updated values for the blog post fields
    such as title, body, and published
    :type request: schemas.Blog
    :param db: Session is an instance of the SQLAlchemy Session class, which represents a transactional
    database connection. It is used to interact with the database and perform CRUD (Create, Read,
    Update, Delete) operations on the database. The Session object is created by the SQLAlchemy engine
    and is passed to the function as a
    :type db: Session
    :return: a string 'updated' after updating the blog with the given id in the database.
    """
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    """
    The function retrieves a blog from the database based on its ID and raises an HTTPException if the
    blog is not found.
    
    :param id: The id parameter is an integer that represents the unique identifier of a blog. It is
    used to query the database and retrieve the blog with the matching id
    :type id: int
    :param db: The "db" parameter is a SQLAlchemy session object that is used to interact with the
    database. It allows the function to query the database and retrieve the blog with the specified ID
    :type db: Session
    :return: a blog object with the given id from the database. If the blog is not found, it raises an
    HTTPException with a 404 status code and a message indicating that the blog is not available.
    """
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog