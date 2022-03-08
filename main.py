from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'data': {'msg': 'Hello World from ROOT'}}


@app.get('/about')
def about():
    return {'msg': 'Deep Learning Practical Applications using HuggingFace and FastAPI Web Framework. Created by Marlon Cajamarca'}
