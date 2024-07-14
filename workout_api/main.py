from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

# Manipulador de exceção para IntegrityError
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_303_SEE_OTHER,
        content={"message": "Já existe um atleta cadastrado com o CPF especificado."}
    )
