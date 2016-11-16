from django.shortcuts import render
from Management.models import News_list
from django.http import HttpResponseRedirect
from Management.pager import Pagination

# Create your views here.

def login(req):
    if req.method == 'GET':
        return render(req, 'home/login.html')
    elif req.method == 'POST':
        if req.POST['username'] == 'alex' and req.POST['password']== 'aaa' and req.POST['checkcode']== 'bbb':
            req.session['islogin'] = True
            return HttpResponseRedirect('/management/1')
        else:
            return render(req, 'home/login.html')


def management(req,page):
    if req.method == 'GET':
        try:
            if not req.session['islogin']:
                return HttpResponseRedirect('/login/')
            else:
                news_list = News_list.objects.all()
                obj = Pagination(page, len(news_list))
                current_list = news_list[obj.start: obj.end]
                str_page = obj.string_pager()
                page = page
                return render(req, 'home/management.html', locals())
        except:
            return HttpResponseRedirect('/login/')
    if req.method == 'POST':
        if News_list.objects.filter(title=req.POST['title'], content=req.POST['content']).values('checked').first()['checked']:
            News_list.objects.filter(title=req.POST['title'],content=req.POST['content']).update(checked=0)
        elif not News_list.objects.filter(title=req.POST['title'], content=req.POST['content']).values('checked').first()['checked']:
            News_list.objects.filter(title=req.POST['title'], content=req.POST['content']).update(checked=1)
        return
