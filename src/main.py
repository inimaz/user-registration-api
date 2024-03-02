from fastapi import FastAPI

app = FastAPI()

# TODO: add the endpoints + logic
@app.get("/")
async def root():
    return {"message": "Hello World"}