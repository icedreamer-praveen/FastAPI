from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import database, models, token
from blog.hashing import Hash

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """
    This function handles user login authentication and returns an access token if the credentials are
    valid.
    
    :param request: The `request` parameter is of type `OAuth2PasswordRequestForm` and is used to
    retrieve the user's email and password from the request body when a user attempts to log in
    :type request: OAuth2PasswordRequestForm
    :param db: The "db" parameter is a dependency injection that provides a database session to the
    function. It is used to query the database for the user with the provided email and to check if the
    password is correct
    :type db: Session
    :return: a dictionary with two keys: "access_token" and "token_type". The value of "access_token" is
    a JWT access token that is created using the user's email as the subject. The value of "token_type"
    is "bearer", which is the type of token being returned.
    """
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    