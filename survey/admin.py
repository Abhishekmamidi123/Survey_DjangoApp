# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from survey.models import FormId, OptionType, Question, Option

admin.site.register(FormId)
admin.site.register(OptionType)
admin.site.register(Question)
admin.site.register(Option)
