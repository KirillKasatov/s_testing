# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=250)
    qset = models.ForeignKey(Test, related_name='questions')

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    text = models.CharField(max_length=250)
    is_true = models.BooleanField()

    def __unicode__(self):
        return self.text


class ActiveTest(models.Model):
    user = models.ForeignKey(User, related_name='tests')
    test = models.ForeignKey(Test)
    results = JSONField(default={})


# class Message(models.Model):
#     user = models.ForeignKey(User)
#     text = models.TextField()
#
#     def __unicode__(self):
#         return self.text