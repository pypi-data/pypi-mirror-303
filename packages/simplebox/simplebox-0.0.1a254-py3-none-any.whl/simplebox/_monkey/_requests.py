#!/usr/bin/env python
# -*- coding:utf-8 -*-
from hyper.contrib import HTTP20Adapter
from requests import PreparedRequest, Response

from .._requests._models import _prepare_headers, _prepare_body, _resp_json
from .._requests._adapter import _build_response

PreparedRequest.prepare_headers = _prepare_headers
PreparedRequest.prepare_body = _prepare_body
Response.json = _resp_json
HTTP20Adapter.build_response = _build_response


