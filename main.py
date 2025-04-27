from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def index():
  return "Hello World!"

@app.get('/test')
def test():
  return {"msg":"這是test", "value":"28"}