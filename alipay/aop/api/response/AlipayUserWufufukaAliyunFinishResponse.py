#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserWufufukaAliyunFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserWufufukaAliyunFinishResponse, self).__init__()
        self._retry_flag = None

    @property
    def retry_flag(self):
        return self._retry_flag

    @retry_flag.setter
    def retry_flag(self, value):
        self._retry_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserWufufukaAliyunFinishResponse, self).parse_response_content(response_content)
        if 'retry_flag' in response:
            self.retry_flag = response['retry_flag']
