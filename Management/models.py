from django.db import models

# Create your models here.

class SendMsg(models.Model):
    code = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    times = models.IntegerField(default=0)
    ctime = models.TimeField()


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    ctime = models.TimeField()


class NewsType(models.Model):
    caption = models.CharField(max_length=32)


class News(models.Model):
    user_info_id = models.ForeignKey('UserInfo')
    news_type_id = models.ForeignKey("NewsType")
    ctime = models.TimeField()
    title = models.CharField(max_length=32)
    url = models.URLField()
    content = models.CharField(max_length=256)
    favor_count = models.IntegerField()
    comment_count = models.IntegerField()


class Favor(models.Model):
    user_info_id = models.ForeignKey("UserInfo")
    news_id = models.ForeignKey("News")
    ctime = models.TimeField()


class Comment(models.Model):
    user_info_id = models.ForeignKey("UserInfo")
    news_id = models.ForeignKey("News")
    reply_id = models.ForeignKey("Comment")
    up = models.IntegerField
    down = models.IntegerField
    ctime = models.TimeField
    device = models.CharField(max_length=63)
    content = models.CharField(max_length=256)
