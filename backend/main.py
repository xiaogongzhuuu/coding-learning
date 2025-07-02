from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():
    return{"wellcome to my homepage"}
@app.get("/user/{name}")
def getname(name):
    return {"hello" + name}
@app.get("/square/{number}")
def square(number):
    number=int(number)
    return{"result":number*number}

