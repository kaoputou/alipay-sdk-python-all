#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeAddModel(object):

    def __init__(self):
        self._employee_email = None
        self._employee_mobile = None
        self._employee_name = None
        self._employee_no = None
        self._enterprise_id = None
        self._identity = None
        self._identity_type = None
        self._role_list = None

    @property
    def employee_email(self):
        return self._employee_email

    @employee_email.setter
    def employee_email(self, value):
        self._employee_email = value
    @property
    def employee_mobile(self):
        return self._employee_mobile

    @employee_mobile.setter
    def employee_mobile(self, value):
        self._employee_mobile = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def role_list(self):
        return self._role_list

    @role_list.setter
    def role_list(self, value):
        if isinstance(value, list):
            self._role_list = list()
            for i in value:
                self._role_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.employee_email:
            if hasattr(self.employee_email, 'to_alipay_dict'):
                params['employee_email'] = self.employee_email.to_alipay_dict()
            else:
                params['employee_email'] = self.employee_email
        if self.employee_mobile:
            if hasattr(self.employee_mobile, 'to_alipay_dict'):
                params['employee_mobile'] = self.employee_mobile.to_alipay_dict()
            else:
                params['employee_mobile'] = self.employee_mobile
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.role_list:
            if isinstance(self.role_list, list):
                for i in range(0, len(self.role_list)):
                    element = self.role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_list[i] = element.to_alipay_dict()
            if hasattr(self.role_list, 'to_alipay_dict'):
                params['role_list'] = self.role_list.to_alipay_dict()
            else:
                params['role_list'] = self.role_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeAddModel()
        if 'employee_email' in d:
            o.employee_email = d['employee_email']
        if 'employee_mobile' in d:
            o.employee_mobile = d['employee_mobile']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'role_list' in d:
            o.role_list = d['role_list']
        return o

