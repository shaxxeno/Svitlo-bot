from aiogram import Router

from . import basic
from . import save_address
from . import get_info

router = Router(name='handlers_router')

router.include_routers(
    basic.router,
    save_address.router,
    get_info.router,
)