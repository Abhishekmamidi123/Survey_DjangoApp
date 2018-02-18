# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from survey.models import FormId, OptionType, Question, Option
from django.shortcuts import redirect
import json

def createSurvey(request):
    if request.method == 'POST':
        print '==========================111111111111============================'
        print '\n'
        print '----------------------'
        print '\n'
        # print json.loads(request.POST)
        print '\n'
        print type(request.POST.get('Data'))
        print request.POST
        # print request.POST.get('Data')[0]
        print '\n'
        print json.dumps(request.POST)
        print '\n'
        print request.body
        # data = {x: request.POST.get(x) for x in request.POST.keys()}
        # print '\n'
        # print data
        # print '\n'
        print '----------------------'
        print '\n'
        return redirect('/survey/thankyou/')
        # return render(request, 'survey/thank-you.html', None)
    else:
        return render(request, 'survey/create_survey.html', None)

def takeSurvey(request):
    dummy_form = []
    pk = 1
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
        dummy_form.append(Question_list)
    boolValue = False
    if request.method == 'POST':
        data = []
        count=1
        print dummy_form[0]['option_type']
        for question in dummy_form:
            q = questions_list[count-1]
            options_objects = options_list.filter(question_id = q.pk)
            if question['option_type'] == 'radio_button':
                selected_option = request.POST['selected_option_r'+str(count)]
                data.append(request.POST['selected_option_r'+str(count)])
                l = options_objects.filter(option_text=selected_option)[0]
                l.count = l.count + 1
                l.save()

            elif question['option_type'] == 'drop_down':
                selected_option = request.POST['selected_option_dd'+str(count)]
                data.append(request.POST['selected_option_dd'+str(count)])
                l = options_objects.filter(option_text=selected_option)[0]
                l.count = l.count + 1
                l.save()

            elif question['option_type'] == 'multi_select':
                selected_options = request.POST.getlist('selected_option_ms'+str(count))
                data.append(request.POST.getlist('selected_option_ms'+str(count)))
                for selected_option in selected_options:
                    l = options_objects.filter(option_text=selected_option)[0]
                    l.count = l.count + 1
                    l.save()

            elif question['option_type'] == 'two_text_boxes':
                data.append(request.POST['text_area_1'+str(count)])
                data.append(request.POST['text_area_2'+str(count)])
                textArea1 = request.POST['text_area_1'+str(count)]
                textArea2 = request.POST['text_area_2'+str(count)]
                print 'text_area_1'+str(count)
                l = options_objects[0]
                l.option_text = textArea1
                l.save()
                m = options_objects[1]
                m.option_text = textArea2
                m.save()
            count+=1
        boolValue = True
        context={'data':data, 'boolValue':boolValue}
    else:
        form = dummy_form
        data = []
        context={'form':form, 'data':data, 'boolValue':boolValue}
    return render(request, 'survey/take_survey.html', context)

def thankyou(request):
    return render(request, 'survey/thank-you.html', None)
