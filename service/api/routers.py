from fastapi import APIRouter

from . import v1


router = APIRouter()
router.include_router(v1.router, prefix='/v1')


@router.get('/health-check')
async def health_check():
    return {'status': 'ok'}
