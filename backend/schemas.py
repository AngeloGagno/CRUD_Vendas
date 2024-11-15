from pydantic import BaseModel, PositiveFloat, EmailStr
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    email: EmailStr

# Create
class ProductCreate(ProductBase):
    pass

# Get
class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Update
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    email: Optional[str] = None

