
from ...services.configCache import get_upload_path
from .utils import resize_image, screenshot, getTempFileName
from co6co .utils import log
from ..base_view import AuthMethodView
import json
import io
import os
from PIL import Image
from io import BytesIO
import requests
from sanic import Request
from sanic.response import text, raw, empty, file, file_stream, ResponseStream
from ...model.pos.resource import resourcePO
from co6co_db_ext.db_utils import QueryOneCallable
from sqlalchemy.sql import Select


class resource_baseView(AuthMethodView):
    async def getRersourcePath(self, request: Request, path):
        uploadRoot = await get_upload_path(request)
        fullPath = os.path.join(uploadRoot, path[1:])
        return os.path.abspath(fullPath)

    async def getLocalPathById(self, request: Request, pk: int) -> str:
        call = QueryOneCallable(self.get_db_session(request))
        data = await call(Select(resourcePO.url).filter(resourcePO.id == pk), isPO=False)
        if data != None:
            return await self.getRersourcePath(request, data["url"])
        return None

    async def getLocalPath(self, request: Request) -> str:
        path = ""
        for k, v in request.query_args:
            if k == "path":
                path = v
        if path.startswith("http"):
            return path
        return await self.getRersourcePath(request, path)

    async def screenshot(self, fullPath: str, w: int = 208, h: int = 117, isFile: bool = True):
        """
        视频截图
        视频第一帧作为 poster
        """
        if fullPath.startswith('http') or os.path.exists(fullPath):
            isFile = not fullPath.startswith('http')
            tempPath = await screenshot(fullPath, w, h, isFile=isFile, useBytes=True)
            if tempPath == None:
                return empty(status=404)
            return raw(tempPath,  status=200, headers=None,  content_type="image/jpeg")
        return empty(status=404)

    async def readHttpImage(self, url):
        data = requests.get(url)
        if data.status_code == 200:
            data = BytesIO(data.content)
            im = Image.open(data)
            return im
        return None

    async def readLocalImage(path):
        if os.path.exists(path):
            im = Image.open(path)
            return im
        return None

    async def screenshot_image(self, fullPath: str, w: int = 208, h: int = 117):
        """ 
        略缩图
        """
        im = None
        if fullPath.startswith('http'):
            im = await self.readHttpImage(fullPath)
        elif os.path.exists(fullPath):
            im = await self.readLocalImage(fullPath)
        if im != None:
            bytes = io.BytesIO()
            im.thumbnail((w, h))
            im.save(bytes, "PNG")
            return raw(bytes.getvalue(),  status=200, headers=None,  content_type="image/jpeg")
        return empty(status=404)
