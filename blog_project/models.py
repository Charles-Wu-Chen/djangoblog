# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Answer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    authoruserid = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    answerlink = models.CharField(max_length=200, blank=True, null=True)
    questionid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class Question(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionlink = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question'


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    userlinkid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserFollower(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField(blank=True, null=True)
    followerid = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_follower'


class UserLikeAnswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    answerid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_like_answer'
