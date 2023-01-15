#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CfbudmacBizActionLogDTO import CfbudmacBizActionLogDTO


class MyxiaojinFinanceBudgetReturnResponse(AlipayResponse):

    def __init__(self):
        super(MyxiaojinFinanceBudgetReturnResponse, self).__init__()
        self._result_data = None
        self._result_msg = None

    @property
    def result_data(self):
        return self._result_data

    @result_data.setter
    def result_data(self, value):
        if isinstance(value, CfbudmacBizActionLogDTO):
            self._result_data = value
        else:
            self._result_data = CfbudmacBizActionLogDTO.from_alipay_dict(value)
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(MyxiaojinFinanceBudgetReturnResponse, self).parse_response_content(response_content)
        if 'result_data' in response:
            self.result_data = response['result_data']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
