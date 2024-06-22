"""A small microservice that provides a web interface to the math_code.py
module. Uses FastAPI and Uvicorn.
"""

from fastapi import FastAPI
from math_code import add, sub, mul, div

app = FastAPI()

# build out routes for each imported function
@app.get("/add/{a}/{b}")
def add_route(a: int, b: int):
    return add(a, b)


@app.get("/sub/{a}/{b}")
def sub_route(a: int, b: int):
    return sub(a, b)


@app.get("/div/{a}/{b}")
def div_route(a: int, b: int):
    return div(a, b)


@app.get("/mul/{a}/{b}")
def mul_route(a: int, b: int):
    return mul(a, b)


@app.get("/")
async def root():
    return {"message": "Go to http://localhost:8080/docs to see the FastAPI"}


# run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
