#uvicorn backend.main:app
from typing import Annotated
from fastapi import FastAPI,Path,Query
from fastapi.responses import RedirectResponse , FileResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI()


@app.get("/member")
def member():
    return RedirectResponse("/")

#处理路径/hello？name=名字
@app.get("/hello")
def hello(name):
    message="hello "+name
    return{"message":message}

#/multiply?n1=1&n2=2
@app.get("/multiply")
def multiply(
    n1:Annotated[int,None],
    n2:Annotated[int,None]
):
    n=int(n1)*int(n2)
    return{"result":n}

#/user/
@app.get("/user/{name}")
def getname(name):
    return {"hello" + name}

@app.get("/square")
def square(number:Annotated[int,None]):
    number=int(number)
    return{"result":number*number}


app.mount("/",StaticFiles(directory="frontend",html=True))


