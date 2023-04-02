from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: Optional[int] = 10, published: Optional[bool] = True
          ):
    if published:
        return {'data': f'{limit} published blog(s) from db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unplublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(req: Blog):
    return {'data': f'blog is created with title {req.title}'}
