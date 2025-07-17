import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="aA123ZXCVBNM",
    host="sydeMacBook-Air.local",
    database="fastapi"
)
print("database ready")






#uvicorn backend.main:app

from typing import Annotated
from fastapi import FastAPI,Path,Query,Body
from fastapi.responses import RedirectResponse , FileResponse
#from fastapi.staticfiles import StaticFiles

app=FastAPI()

@app.get("/createMessage")
def createmessage(
    author:Annotated[str,None],
    content:Annotated[str,None]
):
    
    cursor=con.cursor()
    cursor.execute()








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

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# get 请求
@app.get("/test")
def gettest():
    return {"get":True}

#post 请求
@app.post("/test")
def posttest(body=Body(None)):
    print(body)
    return {"post":True}










# app.mount("/",StaticFiles(directory="frontend",html=True))