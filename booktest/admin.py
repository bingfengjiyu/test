from django.contrib import admin
from booktest.models import BookInfo,Hero
# Register your models here.
# 后台管理界面
class BookInfoAdnin(admin.ModelAdmin):
    list_display = ["id","btitle","bpub_date"]

class HeroAdmin(admin.ModelAdmin):
    list_display = ["id","hname","hage","hcomment","hbook"]

admin.site.register(BookInfo,BookInfoAdnin)
admin.site.register(Hero,HeroAdmin)