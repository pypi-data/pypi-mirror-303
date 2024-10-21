
from sanic import Request
from sqlalchemy.sql import Select
from co6co.utils import log
from sqlalchemy.ext.asyncio import AsyncSession
from .baseCache import BaseCache
from co6co_db_ext.db_utils import DbCallable, db_tools
from ..model.pos.other import sysConfigPO


async def get_upload_path(request: Request) -> str:
    """
    获取上传路径
    数据库未配置使用 /upload
    """
    key = "SYS_CONFIG_UPLOAD_PATH"
    cache = ConfigCache(request)
    path = cache.getConfig(key)
    if path == None:
        await cache.queryConfig(key)
        path = cache.getConfig(key)
    if path == None:
        path = "/upload"
        log.warn("未配置上传路径:key:{},使用默认值:{}".format(key, path))
    return path


class ConfigCache(BaseCache):

    def __init__(self, request: Request) -> None:
        super().__init__(request)

    @property
    def configKeyPrefix(self):
        return 'ConfigKey'

    def getKey(self, code: str):
        """
        获取Key
        """
        return "{}_{}".format(self.configKeyPrefix, code)

    async def queryConfig(self, code: str):
        """
        查询当前用户的所拥有的角色
        结果放置在cache中
        """
        callable = DbCallable(ConfigCache.session(self.request))

        async def exe(session):
            select = (
                Select(sysConfigPO.name, sysConfigPO.code,
                       sysConfigPO.value, sysConfigPO.remark)
                .filter(sysConfigPO.code.__eq__(code))
            )
            data: dict | None = await db_tools.execForMappings(session, select, queryOne=True)
            if data == None:
                log.warn("query {} config is NULL".format(code))
            else:
                self.setConfig(code, data.get("value"))
        await callable(exe)

    def setConfig(self, code: str, value: str):
        if code != None:
            self.setCache(self.getKey(code), value)

    def getConfig(self, code: str) -> str | None:
        if code != None:
            return self.getCache(self.getKey(code))

    def clear(self, code: str) -> str | None:
        if code != None:
            return self.remove(self.getKey(code))
