from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

posts: list[dict]=[
    {
  "id": 1,
  "author": "Vic",
  "title": "My First Post",
  "content": "Learning JSON in Python is simple and powerful.",
  "date_posted": "2026-05-12"
},
{
  "id": 2,
  "author": "Amina",
  "title": "API Basics",
  "content": "Endpoints connect frontend and backend systems.",
  "date_posted": "2026-05-10"
}
]


@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts")
async def home():
    return f"<h1> This is my first API</h1> <br> <p1>{posts[0]['title']}</p1>"

@app.get("/app/posts")
async def get_posts():
    return posts
