#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from app01.models import *
from static.plugin.check_code import check_code
import io

# Create your views here.

def login(req):
    if req.method == 'GET':
        return render(req, 'home/login.html')
    elif req.method == 'POST':
        if req.POST['checkcode'] == req.session['checkcode']:
        # if req.POST['username'] == 'alex' and req.POST['password']== 'aaa' and req.POST['checkcode']== 'bbb':
            if UserInfo.objects.filter(username=req.POST['username'],password=req.POST['password']):
                req.session['islogin'] = True
                return HttpResponseRedirect('/management/')
        else:
            return render(req, 'home/login.html')

def index(req):
    if req.method == 'GET':
        try:
            if not req.session['islogin']:
                return HttpResponseRedirect('/login/')
            else:
                news_list = News.objects.all()
                return render(req, 'home/index.html', locals())
        except:
            return HttpResponseRedirect('/client/login/')
    if req.method == 'POST':
        if News.objects.filter(title=req.POST['title'], content=req.POST['content']).values('checked').first()[
            'checked']:
            News.objects.filter(title=req.POST['title'], content=req.POST['content']).update(checked=0)
        elif not \
        News.objects.filter(title=req.POST['title'], content=req.POST['content']).values('checked').first()[
            'checked']:
            News.objects.filter(title=req.POST['title'], content=req.POST['content']).update(checked=1)

def checkcode(req):
    # 生成图片并且返回
    mstream = io.BytesIO()
    # 创建图片，并写入验证码
    img, code = check_code.create_validate_code()
    # 将图片对象写入到mstream，
    img.save(mstream, "GIF")
    # 为每个用户保存其验证码
    req.session["checkcode"] = code
    # self.write(mstream.getvalue())
    return HttpResponse(mstream.getvalue())
    # return HttpResponse('OK')