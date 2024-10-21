
from sanic import Request
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import Select
from co6co.utils import log
from sqlalchemy.ext.asyncio import AsyncSession
from co6co_web_db.services.cacheManage import CacheManage
from . import getCurrentUserId, getSecret, generateCode


class BaseCache(CacheManage):
    userId: int
    request = Request

    def __init__(self, request: Request) -> None:
        # 微信认证中 userid可能为挂在上去
        self.userId = getCurrentUserId(request)
        self.request = request
        super().__init__(request.app)
