# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from survey.models import FormId, OptionType, Question, Option

def createSurvey(request):
    return render(request, 'survey/create_survey.html', None)

def takeSurvey(request):
    form = []
    pk = 2
    questions_list = Question.objects.filter(form_id = pk)
    options_list = Option.objects.all()
    for question in questions_list:
        Question_list = {}
        Question_list['question_text'] = question.question_text
        Question_list['option_type'] = question.option_type.option_type
        options = options_list.filter(question_id = question.pk)
        list_of_options = []
        for option in options:
            list_of_options.append(option.option_text)
        Question_list['options'] = list_of_options
        form.append(Question_list)
    context={'form':form}
    return render(request, 'survey/take_survey.html', context)
