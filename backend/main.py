from typing import Annotated
from fastapi import FastAPI,Path,Query
app=FastAPI()
@app.get("/")
def index():
    return{"wellcome to my homepage"}
#处理路径/hello？name=名字
@app.get("/hello")
def hello(name):
    message="hello "+name
    return{"message":message}
#/multiply?n1=1&n2=2
@app.get("/multiply")
def multiply(n1,n2):
    n=int(n1)*int(n2)
    return{"result":n}
#/user/
@app.get("/user/{name}")
def getname(name):
    return {"hello" + name}
@app.get("/square/{number}")
def square(number):
    number=int(number)
    return{"result":number*number}


