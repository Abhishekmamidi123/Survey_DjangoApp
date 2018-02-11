# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FormId(models.Model):
    form_id = models.AutoField(primary_key=True)

class OptionType(models.Model):
    option_type = models.CharField(max_length=255, unique=True)

class Questions(models.Model):
    question_text = models.TextField(blank=True, default="")
    option_type = models.ForeignKey(OptionType)
    form_id = models.ForeignKey(FormId, related_name = "form_questions")

class Options(models.Model):
    option_text = models.CharField(max_length=255, unique=True)
    question_id = models.ForeignKey(Questions)
