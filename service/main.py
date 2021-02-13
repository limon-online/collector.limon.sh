from fastapi import FastAPI

from api import router


app = FastAPI(
    title='Collector',
    description='This is an API for collect date from agents',
    version='0.0.1'
)

app.include_router(router, prefix='/api')
