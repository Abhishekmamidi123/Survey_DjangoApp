# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def createSurvey(request):
    return render(request, 'survey/create_survey.html', None)

def takeSurvey(request):
    return render(request, 'survey/take_survey.html', None)
