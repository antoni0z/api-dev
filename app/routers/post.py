from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas,oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/posts",
    tags = ['Posts']

)

@router.get("/",response_model = List[schemas.Postout])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),limit: int = 10,skip: int = 0,search: Optional[str] = ""):
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    #print(limit)
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts 


@router.post("/",status_code = 201, response_model = schemas.Post)

def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #print(user_id)
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    #cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content,post.published))
    #conn.commit()
    #new_post = cursor.fetchone()
    return new_post
    
# title str, content str

@router.get("/{id}",response_model = schemas.Postout) #{id} represents a path parameter. 
def get_post(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): #Fast API validation and conversion of the type
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
    #cursor.execute("""SELECT * FROM posts WHERE id = %s """,([str(id)]))
    #post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} wasn't found")
    return post

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # Deleting Post
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",([str(id)]))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} doesn't exist")

    if post_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "Not authorized to perform requested action")

    post_query.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model = schemas.Post)
def update_post(id: int, post: schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title, post.content,post.published,id))
    #updated_post = cursor.fetchone()
    #conn.commit()
    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} doesn't exist")

    if post_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = "Not authorized to perform requested action")

    post_query.update(post.dict(),synchronize_session = False)

    db.commit()
    return post_query.first()