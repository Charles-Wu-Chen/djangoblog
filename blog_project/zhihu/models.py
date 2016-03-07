from django.db import models

# Create your models here.

class ZhihuUser (models.Model):
    #id is auto by django
    userName = models.CharField(max_length=250)
    userLinkId = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserFollower(models.Model):
    userId = models.ForeignKey(ZhihuUser, related_name='user')
    followerId = models.ForeignKey(ZhihuUser, related_name='follower')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Question(models.Model):
    questionlink = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    authoruserid = models.ForeignKey(ZhihuUser)
    answerlink = models.CharField(max_length=200, blank=True, null=True)
    questionid = models.ForeignKey(Question)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserLikeAnswer(models.Model):
    userid = models.ForeignKey(ZhihuUser)
    answerid = models.ForeignKey(Answer)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
