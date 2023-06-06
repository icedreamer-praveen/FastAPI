from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from blog import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    """
    This function returns the current user by verifying the provided token using OAuth2 scheme.
    
    :param data: The parameter `data` is of type `str` and is used to receive the token passed in the
    request header. It is used as input to the `get_current_user` function
    :type data: str
    :return: The function `get_current_user` returns the result of calling the `token.verify_token`
    function with the `data` parameter as input, and the `credentials_exception` parameter as the second
    parameter. The `verify_token` function will either return the decoded token if it is valid, or raise
    an exception if it is not valid. If an exception is raised, it will be the `credentials_exception
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception)