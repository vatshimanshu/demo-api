from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/demo-app")
def hello():
  return {"Hello world!"}


@app.get("/demo-app-name/")
def hello(name:str):
  greet = "Hello " + name + "!"

  t = time.localtime()
  curr = time.strftime("%H:%M:%S", t)
  
  return {"greet":greet, "time": curr}
