from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

class Post(BaseModel):
    title:str
    content:str
    published: bool= True
    rate:Optional[int]=None


my_posts=[{"title":"Title of post 1","content":"content of post 1","id":1},{"title":"Favorite foods","content":"I like food","id":2}]

def find_posts(id):
    for p in my_posts:
        if p["id"]==id:
            return p

    

app=FastAPI()

@app.get("/")
async def home():
    return {"Welcome":"This is the home page"}

@app.get("/posts")
async def posts():
    return{"data":my_posts}

@app.post("/posts")
async def create_posts(post:Post):
    post_dict=post.model_dump()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/{id}")
async def get_posts(id: int):
    post=find_posts(id)
    return {"post_detail":post}