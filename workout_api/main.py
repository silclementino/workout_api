from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import add_pagination
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

# Adicionar paginação
add_pagination(app)

# Manipulador de exceção para IntegrityError
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_303_SEE_OTHER,
        content={"message": "Já existe um atleta cadastrado com o CPF especificado."}
    )
