# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FormId(models.Model):
    form_id = models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.form_id)

class OptionType(models.Model):
    option_type = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.option_type

class Question(models.Model):
    question_text = models.TextField(blank=True, default="")
    option_type = models.ForeignKey(OptionType)
    form_id = models.ForeignKey(FormId, related_name = "form_questions")
    def __str__(self):
        return str(self.question_text) + " --> " + str(self.option_type)

class Option(models.Model):
    option_text = models.CharField(max_length=255, unique=True)
    question_id = models.ForeignKey(Question)
    def __str__(self):
        return str(self.option_text)
