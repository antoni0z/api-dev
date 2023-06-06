from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from .config import settings
#After finishing I can do a project with the document app and do an MVP on the browser. 

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
#If you want to make it public [*]
#If its for a webapp, you want to make sure that your webapp will be the only origin. 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") # This is a decorator. Turns it intos an aPI. And the inside is the Path. 
def root(): #Can be named whatever, better if describes the opeation is doing. 
    return {"message": "Welcome to my API!"}