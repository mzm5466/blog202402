#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from api.jwt_auth import parse_payload
from django.conf import settings
import re
class MD_source(MiddlewareMixin):
    def process_request(self,request):
        current_url = request.path_info
        print(current_url)
        # 白名单校验
        for white_url in settings.VALID_URL_LIST:
            print(re.match(white_url,current_url))
            if re.match(white_url,current_url):
                return None
        try:
            print(request.META)
            auth = request.META.get('HTTP_TOKEN', '')
            print(auth)
            # auth = authorization.split()
        except AttributeError:
            return JsonResponse({"code": 401, "message": "No authenticate header"})

        # 用户通过API获取数据验证流程
        if not auth:
            print(1111)
            return JsonResponse({'error': '未获取到Authorization请求头', 'status': False})
        if len(auth) == 1:
            print(2222)
            return JsonResponse({'error': "非法Authorization请求头", 'status': False})
        result = parse_payload(auth)
        return JsonResponse(result)

    def process_response(self, request, response):
        print("MD1里面的 process_response")
        return response
