from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_all_products,
    get_unique_product,
    delete_product,
    update_product,
)

router = APIRouter()

@router.get("/products/", response_model= List[ProductResponse])
def get_all_products_router(db:Session = Depends(get_db)):
    all_products = get_all_products(db)
    return all_products

@router.get("/products/{product_id}", response_model= ProductResponse)
def get_a_product_router(product_id: int, db:Session = Depends(get_db)):
    product = get_unique_product(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404,detail='Product Not Found')
    return product

@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.put("/products/{product_id}",response_model= ProductResponse)
def update_product_router(product_id:int,product: ProductUpdate, db:Session = Depends(get_db)):
    product_update = update_product(db,product_id=product_id,product=product)
    if product_update is None:
        raise HTTPException(status_code=404,detail='Product Not Found')
    return product_update

@router.delete("/products/{product_id}",response_model= ProductResponse)
def delete_product_router(product_id:int,db:Session = Depends(get_db)):
    deleted_product = delete_product(db=db,product_id=product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404,detail='Product Not Found')
    return deleted_product