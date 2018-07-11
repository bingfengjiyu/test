from django.shortcuts import render
from booktest.models import BookInfo
from django.http import HttpResponse
# Create your views here.
# 将数据库查到的信息返回给模板
def index(request):
    booklist=BookInfo.objects.all()
    return render(request,"booktest/index.html",{'booklist':booklist})


def detail(request,bid):
    book=BookInfo.objects.get(id=int(bid))
    heros=book.hero_set.all()
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})
