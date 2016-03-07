# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('answerlink', models.CharField(max_length=200, blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('questionlink', models.CharField(max_length=200, blank=True, null=True)),
                ('subject', models.CharField(max_length=200, blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeAnswer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('answerid', models.ForeignKey(to='zhihu.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='ZhihuUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('userName', models.CharField(max_length=250)),
                ('userLinkId', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='userlikeanswer',
            name='userid',
            field=models.ForeignKey(to='zhihu.ZhihuUser'),
        ),
        migrations.AddField(
            model_name='userfollower',
            name='followerId',
            field=models.ForeignKey(to='zhihu.ZhihuUser', related_name='follower'),
        ),
        migrations.AddField(
            model_name='userfollower',
            name='userId',
            field=models.ForeignKey(to='zhihu.ZhihuUser', related_name='user'),
        ),
        migrations.AddField(
            model_name='answer',
            name='authoruserid',
            field=models.ForeignKey(to='zhihu.ZhihuUser'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionid',
            field=models.ForeignKey(to='zhihu.Question'),
        ),
    ]
