from models import ProductModel
from schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session

# GET - Unique
def get_unique_product(db: Session, product_id: int):
    """
    db : Cria uma sessao para realizar a query no banco de dados
    product_id : Id do produto buscado
    Fazendo o get de apenas um produto no banco de dados
    """

    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# GET - All
def get_all_products(db: Session):
    """
    db : Cria uma sessao para realizar a query no banco de dados
    Funcao para realizar a busca de todos os Produtos no banco - Select * from df
    """
    return db.query(ProductModel).all()

# Create 
def create_product(db: Session, product: ProductCreate):
    """
    Funcao para criar no banco um produto passado pelo usuário

    db : Cria uma sessao para realizar a query no banco de dados    

    product : Produto que o usuario irá passar para o banco de dados através do escopo da classe
    """
    # Transformar a View que vem do Pydantic para o Database
    db_product = ProductModel(**product.model_dump()) # Desempacotador (**product.model_dump()) - Pydantic para ProductModel(DB)
    # Inserir no banco de dados essa inforcao
    db.add(db_product)
    db.commit()
    # Fazer o refresh(atualizacao) do banco
    db.refresh(db_product)

    return db_product

#UPDATE
def update_product(db:Session, product_id:int, product: ProductUpdate):
    """
    db : Cria uma sessao para realizar a query no banco de dados 

    product_id : Id do produto que deseja alterar

    product : Alteracao no Produto que o usuario irá passar para o banco de dados através do escopo da classe Update
    """
    # realizar a query filtrando o produto selecionado
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first() 

    # verificar qual alteracao foi realizada e realiza-la
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.email is not None:
        db_product.email = product.email

    # enviar ao banco de dados
    db.commit()
    return db_product

def delete_product(db: Session, product_id: int):
    """
    db : Cria uma sessao para realizar a query no banco de dados
    product_id : Id do produto buscado
    """

    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
