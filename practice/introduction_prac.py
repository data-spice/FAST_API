from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app=FastAPI()

@app.get("/",include_in_schema=False)
async def home():
    return {"message":"hello world"}


@app.get("/api/posts",response_class=HTMLResponse)
async def posts():
    return f"<h1> Fast api is cool <h1>"