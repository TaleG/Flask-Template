#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_restful import Resource
from app.utils import RET
# from app import models

class Begin(Resource):
    def get(self):
        """
        RESTful初始页测试
        :return:
        """
        return "Hello Begins."
