## To Setup

1. clone FastAPI repository from the link below in your desired location
    git@github.com:icedreamer-praveen/FastAPI.git 
                        or 
    https://github.com/icedreamer-praveen/FastAPI.git

2. create virtual environment for your project
    python3.8 -m venv venv

3. activate virtual environment
    . venv/bin/activate
            or 
    source venv/bin/activate

4. install requirements file
    pip3 install -r requirements.txt

5. run project
    uvicorn blog.main:app --reload

and check the url     
    http://127.0.0.1:8000/docs/
            or 
    http://localhost:8000/docs/