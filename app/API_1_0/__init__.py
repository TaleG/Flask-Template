#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Blueprint
from flask_restful import Api
from . import Begins

# 创建蓝图对象
api_bp = Blueprint("api_1_0", __name__)
api = Api(api_bp)

api.add_resource(Begins.Begin, '/begin', endpoint='begin')