from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit, published: bool):
    """
    The function returns a string indicating the number of published or unpublished blogs from a
    database based on the given limit.
    
    :param limit: The maximum number of blogs to retrieve from the database
    :param published: A boolean parameter that indicates whether to retrieve only published blogs or all
    blogs from the database
    :type published: bool
    :return: A dictionary containing a string with the number of blogs requested and whether they are
    published or not. If `published` is `True`, the string will say "published blogs", otherwise it will
    just say "blogs".
    """
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    """
    The function returns a dictionary containing the string "all unpublished blog".
    :return: A dictionary with a key 'data' and a value 'all unpublished blog'.
    """
    return {'data': 'all unpublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    """
    The function "show" takes an integer argument "id" and returns a dictionary with a key "data" and
    the value of "id".
    
    :param id: The parameter "id" is of type integer and is used as input for the function "show". The
    function returns a dictionary with a key "data" and the value of the input "id"
    :type id: int
    :return: A dictionary with a key "data" and a value of the input integer "id".
    """
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    """
    The function "comments" returns a dictionary with a set of data for a given ID.
    
    :param id: The parameter 'id' is a variable that is being passed as an argument to the function
    'comments'. It is not clear what type of data this parameter is supposed to be, as it is not used
    within the function
    :return: A dictionary with a key "data" and a set of strings {'1', '2'} as its value.
    """
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    """
    The function creates a blog and returns a message with the blog's title.
    
    :param blog: The parameter `blog` is of type `Blog`, which is likely a custom class or data
    structure that represents a blog post. It is being passed as an argument to the `create_blog`
    function
    :type blog: Blog
    :return: a dictionary with a key 'data' and a value that includes the string 'Blog is created with
    title as' followed by the title of the blog object passed as an argument to the function.
    """
    return {'data': f'Blog is created with title as {blog.title}'}
