from sanic import Sanic, Blueprint, Request
from co6co_sanic_ext .api import add_routes
from ..view_model.user import user_ass_view, users_view, user_view, sys_users_view, ticketView
from ..view_model.currentUser import changePwd_view, user_info_view
from ..view_model.login import login_view
from ..view_model.aop.api_auth import authorized
from ..model.enum import user_state
from co6co_db_ext.db_utils import db_tools
from ..model.pos.right import UserPO
from co6co_sanic_ext.model.res.result import Result
from co6co_sanic_ext.utils import JSON_util
from ..view_model.aop import exist

user_api = Blueprint("users_API", url_prefix="/users")
add_routes(user_api, login_view, ticketView)
add_routes(user_api, changePwd_view, user_info_view)
add_routes(user_api, user_ass_view, users_view, user_view, sys_users_view)


@user_api.route("/status", methods=["GET", "POST"])
@authorized
async def getUserStatus(request: Request):
    """
    用户状态
    """
    states = user_state.to_dict_list()
    return JSON_util.response(Result.success(data=states))


@user_api.route("/exist/<userName:str>/<pk:int>", methods=["GET"])
@authorized
async def userExist(request: Request, userName: str, pk: int = 0):
    """
    用户名是否存在
    """
    result = await db_tools.exist(request.ctx.session, UserPO.userName == userName, UserPO.id != pk)
    return exist(result, "用户", userName)


@user_api.route("/exist", methods=["POST"])
@authorized
async def userExistPost(request: Request):
    """
    用户名是否存在
    """
    id = request.json.get("id")
    userName = request.json.get("userName")
    result = await db_tools.exist(request.ctx.session, UserPO.userName == userName, UserPO.id != id)
    return exist(result, "用户", userName)
