from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from lesson_1 import posts
app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse(
    "home.html",
    {
        "request": request,
        "posts": posts,
        "title": "Home"
    }
)