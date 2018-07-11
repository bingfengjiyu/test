from django.db import models

# Create your models here.
# 数据库建表和字段
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateField()

    def __str__(self):
        return self.btitle


class Hero(models.Model):
    hname=models.CharField(max_length=20)
    hsex=models.BooleanField(default=False)
    hage=models.IntegerField()
    hcomment=models.CharField(max_length=128)
    hbook=models.ForeignKey("BookInfo")

    def __str__(self):
        return self.hname
