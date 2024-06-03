#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemSkuAttrVO import ItemSkuAttrVO


class LocalItemSkuModifyVO(object):

    def __init__(self):
        self._original_price = None
        self._out_sku_id = None
        self._sale_price = None
        self._sale_status = None
        self._sku_attrs = None
        self._sku_id = None
        self._stock_num = None
        self._thumb_img_id = None

    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def sku_attrs(self):
        return self._sku_attrs

    @sku_attrs.setter
    def sku_attrs(self, value):
        if isinstance(value, list):
            self._sku_attrs = list()
            for i in value:
                if isinstance(i, ItemSkuAttrVO):
                    self._sku_attrs.append(i)
                else:
                    self._sku_attrs.append(ItemSkuAttrVO.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def thumb_img_id(self):
        return self._thumb_img_id

    @thumb_img_id.setter
    def thumb_img_id(self, value):
        self._thumb_img_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.sku_attrs:
            if isinstance(self.sku_attrs, list):
                for i in range(0, len(self.sku_attrs)):
                    element = self.sku_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attrs[i] = element.to_alipay_dict()
            if hasattr(self.sku_attrs, 'to_alipay_dict'):
                params['sku_attrs'] = self.sku_attrs.to_alipay_dict()
            else:
                params['sku_attrs'] = self.sku_attrs
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.thumb_img_id:
            if hasattr(self.thumb_img_id, 'to_alipay_dict'):
                params['thumb_img_id'] = self.thumb_img_id.to_alipay_dict()
            else:
                params['thumb_img_id'] = self.thumb_img_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocalItemSkuModifyVO()
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sku_attrs' in d:
            o.sku_attrs = d['sku_attrs']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'thumb_img_id' in d:
            o.thumb_img_id = d['thumb_img_id']
        return o


