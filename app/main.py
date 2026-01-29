from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import get_db
from app.api.v1.route import api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION, 
    description="API para gerenciamento de uma biblioteca, incluindo usuários, livros e empréstimos.",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_router)

@app.get('/', tags=["Root"])
def read_root():
  """
  Rota raiz da API.
  Retorna informações básicas sobre a aplicação.
  """
  return {
      "app_name": settings.APP_NAME,
      "version": settings.APP_VERSION,
      "status": "running",
      "message": "Bem-vindo à API da Biblioteca! Acesse /docs para ver a documentação.",
      "docs": "/docs",
      "health_check": "/health"
  }


@app.get("/health", tags=["Health"])
async def health_check(db: AsyncSession = Depends(get_db)):
  """
  Verifica o status da aplicação e a conexão com o banco de dados.
  """
  try:
    # Testa a conexão com o banco executando uma query simples
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()
    
    if value == 1:
      return {
        "status": "healthy",
        "database": "connected",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION
      }
    else:
      raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Banco de dados retornou resultado inesperado"
      )
  
  except Exception as e:
    raise HTTPException(
      status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
      detail=f"Erro ao conectar com o banco de dados: {str(e)}"
    )
