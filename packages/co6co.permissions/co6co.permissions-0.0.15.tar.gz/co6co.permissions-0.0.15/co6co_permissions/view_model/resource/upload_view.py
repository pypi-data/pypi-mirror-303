
from sanic import Request
from sanic.response import file
from sanic.request.form import File
from sqlalchemy.orm import selectinload
from co6co.utils import log
from . import resource_baseView
from ...services.configCache import get_upload_path
from co6co_sanic_ext.model.res.result import Result
from ...model.pos.resource import resourcePO, userResourcePO
from ...model.enum import resource_category
from co6co.utils import hash, getDateFolder
import uuid
import os
from datetime import datetime
from co6co_db_ext.db_utils import DbCallable, db_tools

from sqlalchemy.sql import Select
from sqlalchemy.ext.asyncio import AsyncSession
from co6co_web_db.view_model import errorLog
from co6co.utils.tool_util import get_current_function_name


class FileResult:
    fullPath: str
    path: str
    hash: str
    name: str
    size: int

    def toPo(self, category: resource_category, subCategory: int = 0):
        po = resourcePO()
        po .uid = uuid.uuid4()
        po .category = category.val
        po .subCategory = subCategory
        po .hash = self.hash
        po .url = self.path
        po .metaName = self.name
        po .size = self.size
        po.createTime = datetime.now()
        return po


class Upload_View(resource_baseView):
    routePath = "/file"

    async def readFileSize(self, file: File):
        """
        获取文件大小
        """
        file_size = 0
        chunk_size = 1024
        while True:
            chunk = file.body.read(chunk_size)
            if not chunk:
                break
            file_size += len(chunk)
        file.body.seek(0)
        return file_size

    async def saveFile(self, request: Request):
        try:
            fullPath = None
            basePath = await get_upload_path(request)
            if "file" not in request.files:
                return self.response_json(Result.fail("No file part in the request"))
            file: File = request.files.get("file")

            size = len(file.body)  # await self. readFileSize(file)
            _, file_extension = os.path.splitext(file.name)
            fileName = getDateFolder(format='%Y-%m-%d-%H-%M-%S')
            fullPath, path = self.getFullPath(basePath, "{}{}".format(fileName, file_extension))
            await self.save_file(file, fullPath)
            result = FileResult()
            result.name = file.name
            result.hash = hash.file_sha256(fullPath)
            result.size = size
            result.fullPath = fullPath
            result.path = path

            return result
        except Exception as e:
            log.warn("保存文件失败：", fullPath, e)
            return self.response_json(Result.fail(message=e))

    async def saveDb(self, request: Request,  param: FileResult, category: resource_category) -> int:
        call = DbCallable(self.get_db_session(request))

        async def exec(session: AsyncSession):
            select = (Select(resourcePO).filter(resourcePO.hash.__eq__(param.hash)) .options(
                selectinload(resourcePO.userResourceList)
            ))

            dbPo: resourcePO = await db_tools.execForPo(session, select, remove_db_instance_state=False)
            userPo = userResourcePO()
            userPo.ownUserId = self.getUserId(request)
            userPo.createTime = datetime.now()
            userPo.name = param.name
            resourceId = None
            # 数据库中已经存在
            if dbPo != None:
                basePath = await get_upload_path(request)
                oldPath = os.path.join(basePath, dbPo.url[1:])
                if os.path.exists(oldPath) and os.path.exists(param.fullPath):
                    os.remove(param.fullPath)
                if not os.path.exists(oldPath):
                    dbPo.url = param.path

                dbPo.userResourceList.append(userPo)
                resourceId = dbPo.id
            else:
                po = param.toPo(category)
                po.userResourceList = [userPo]
                session.add(po)
                await session.flush()
                resourceId = po.id
            return resourceId
        return await call(exec)

    async def putFile(self, request: Request, category: resource_category):
        """
        上传文件
        """
        try:
            result = await self.saveFile(request)
            if type(result) != FileResult:
                return result
            result: FileResult = result
            resourceId = await self.saveDb(request, result, category)
            return self.response_json(Result.success(data={"resourceId": resourceId, "path": result.path}))
        except Exception as e:
            errorLog(request, self.__class__, get_current_function_name())
            return self.response_json(Result.fail(message="上传失败:{}".format(e)))

    async def put(self, request: Request):
        """
        上传文件
        """
        return await self.putFile(request, resource_category.file)


class Image_View(Upload_View):
    routePath = "/img"

    async def put(self, request: Request):
        """
        上传图片
        """
        return await self.putFile(request, resource_category.image)


class Video_View(Upload_View):
    routePath = "/video"

    async def put(self, request: Request):
        """
        上传视频
        """
        return await self.putFile(request, resource_category.video)
