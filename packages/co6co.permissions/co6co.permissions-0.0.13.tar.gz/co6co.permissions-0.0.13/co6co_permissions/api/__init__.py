from sanic import Sanic, Blueprint, Request
from .menu import menu_api
from .userGroup import userGroup_api
from .role import role_api
from .user import user_api
from .view import view_api
from .dict import dict_api
from .config import config_api
from .resource import res_api

permissions_api = Blueprint.group(
    view_api, menu_api, userGroup_api, role_api, user_api, dict_api, config_api, res_api)
