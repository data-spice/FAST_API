from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from data_set import students

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/class_data")
async def root(request:Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
        "title":"Home",
        "students":students
    })

@app.get("/",response_class=HTMLResponse)
async def home():
    return f"<h1>Well Done this is the Root page</h1>"