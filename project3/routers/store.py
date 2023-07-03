import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, APIRouter, Request, Form
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from .auth import get_current_user

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/store",
    tags=["store"],
    responses={404: {"description":"Not found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def read_all_by_user(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    items = db.query(models.Items).filter(models.Items.owner_id == user.get("id")).all()

    return templates.TemplateResponse("home.html", {"request": request, "items": items, "user": user})


@router.get("/add-item", response_class=HTMLResponse)
async def add_new_item(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("add-item.html", {"request": request, "user": user})


@router.post("/add-item", response_class=HTMLResponse)
async def create_item(request: Request, item_name: str = Form(...), cost: float = Form(...), 
                      description: str = Form(...), db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    store_model = models.Items()
    store_model.item_name = item_name
    store_model.cost = cost
    store_model.description = description
    store_model.owner_id = user.get("id")

    db.add(store_model)
    db.commit()

    return RedirectResponse(url="/store", status_code=status.HTTP_302_FOUND)


@router.get("/edit-item/{item_id}", response_class=HTMLResponse)
async def edit_todo(request: Request, item_id: int, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    item = db.query(models.Items).filter(models.Items.id == item_id).first()

    return templates.TemplateResponse("edit-item.html", {"request": request, "item": item, "user": user})


@router.post("/edit-item/{item_id}", response_class=HTMLResponse)
async def edit_todo_commit(request: Request, item_id: int, item_name: str = Form(...),
                           cost: float = Form(...), description: str = Form(...),
                           db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    store_model = db.query(models.Items).filter(models.Items.id == item_id).first()

    store_model.item_name = item_name
    store_model.cost = cost
    store_model.description = description
    
    db.add(store_model)
    db.commit()

    return RedirectResponse(url="/store", status_code=status.HTTP_302_FOUND)


@router.get("/delete/{item_id}")
async def delete_todo(request: Request, item_id: int, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    item_model = db.query(models.Items).filter(models.Items.id == item_id)\
        .filter(models.Items.owner_id == user.get("id")).first()

    if item_model is None:
        return RedirectResponse(url="/Items", status_code=status.HTTP_302_FOUND)

    db.query(models.Items).filter(models.Items.id == item_id).delete()

    db.commit()

    return RedirectResponse(url="/store", status_code=status.HTTP_302_FOUND)