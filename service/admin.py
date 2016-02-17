# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Test, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
