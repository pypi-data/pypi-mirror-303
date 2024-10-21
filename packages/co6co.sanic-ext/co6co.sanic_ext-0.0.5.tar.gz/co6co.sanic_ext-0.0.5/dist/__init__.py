from functools import wraps
from sanic.views import HTTPMethodView  # 基于类的视图
from sanic.request.form import File  # 基于类的视图
from sanic import Request
from co6co_sanic_ext.model.res.result import Page_Result
from co6co_sanic_ext.utils import JSON_util
from typing import TypeVar, Dict, List, Any, Tuple
from co6co_sanic_ext.model.res.result import Result, Page_Result
import aiofiles
import os
import multipart
from io import BytesIO
from sqlalchemy import Select
from co6co_db_ext.po import BasePO, UserTimeStampedModelPO
from datetime import datetime
from co6co.utils.tool_util import list_to_tree, get_current_function_name
from co6co.utils import log, getDateFolder


class BaseView(HTTPMethodView):
    """
    视图基类： 约定 增删改查，其他未约定方法可根据实际情况具体使用
    views.POST  : --> query list
    views.PUT   :---> Add 
    view.PUT    :---> Edit
    view.DELETE :---> del
    """
    """
    类属性：
    路由使用路径
    """
    routePath: str = "/"

    def response_json(self, data: Result | Page_Result):
        return JSON_util.response(data)

    def is_integer(self, s: str | bytes | bytearray):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def usable_args(self, request: Request) -> dict:
        """
        去除列表
        request.args={name:['123'],groups:["a","b"]}
        return {name:'123',groups:["a","b"]}
        """
        args: dict = request.args
        data_result = {}
        for key in args:
            value = args.get(key)
            if len(value) == 1:
                data_result.update({key: value[0]})
            else:
                data_result.update({key: value})
        return data_result

    async def save_body(self, request: Request, root: str):
        # 保存上传的内容
        subDir = getDateFolder(format='%Y-%m-%d-%H-%M-%S')
        filePath = os.path.join(root, getDateFolder(), f"{subDir}.data")
        filePath = os.path.abspath(filePath)  # 转换为 os 所在系统路径
        folder = os.path.dirname(filePath)
        if not os.path.exists(folder):
            os.makedirs(folder)
        async with aiofiles.open(filePath, 'wb') as f:
            await f.write(request.body)
        # end 保存上传的内容

    async def parser_multipart_body(self, request: Request) -> Tuple[Dict[str, tuple | Any], Dict[str, multipart.MultipartPart]]:
        """
        解析内容: multipart/form-data; boundary=------------------------XXXXX,
        的内容
        """
        env = {
            "REQUEST_METHOD": "POST",
            "CONTENT_LENGTH": request.headers.get("content-length"),
            "CONTENT_TYPE": request.headers.get("content-type"),
            "wsgi.input": BytesIO(request.body)
        }
        data, file = multipart.parse_form_data(env)
        data_result = {}
        # log.info(data.__dict__)
        for key in data.__dict__.get("dict"):
            value = data.__dict__.get("dict").get(key)
            if len(value) == 1:
                data_result.update({key: value[0]})
            else:
                data_result.update({key: value})
        # log.info(data_result)
        return data_result, file

    async def save_file(self, file: File, path: str):
        """
        保存上传的文件
        file.name
        """
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        if os.path.exists(path):
            raise Exception("{} Exists".format(path))
        async with aiofiles.open(path, 'wb') as f:
            await f.write(file.body)

    async def _save_file(self, request: Request, *savePath: str, fileFieldName: str = None):
        """
        保存上传的文件
        """
        p_len = len(savePath)
        if fileFieldName != None and p_len == 1:
            file = request.files.get(fileFieldName)
            await self.save_file(file, *savePath)
        elif p_len == len(request.files):
            i: int = 0
            for file in request.files:
                file = request.files.get('file')
                await self.save_file(file, savePath[i])
                i += 1

    def getFullPath(self, root, fileName: str) -> Tuple[str, str]:
        """
        获取去路径和相对路径
        """
        filePath = "/".join(["", getDateFolder(), fileName])
        fullPath = os.path.join(root, filePath[1:])

        return fullPath, filePath
