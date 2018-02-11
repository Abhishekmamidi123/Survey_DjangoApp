# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from survey.models import FormId, OptionType, Question, Option

def createSurvey(request):
    return render(request, 'survey/create_survey.html', None)

def takeSurvey(request):
    pk = 1
    questions_list = Question.objects.filter(form_id = pk)
    # for question in questions_list:

    return render(request, 'survey/take_survey.html', None)
