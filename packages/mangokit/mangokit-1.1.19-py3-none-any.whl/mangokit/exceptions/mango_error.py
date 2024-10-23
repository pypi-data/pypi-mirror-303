# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-09-23 11:03
# @Author : 毛鹏


class MangoKitError(Exception):

    def __init__(self, code: int, msg: str, value: tuple = None):
        if value:
            msg = msg.format(*value)
        self.code = code
        self.msg = msg
