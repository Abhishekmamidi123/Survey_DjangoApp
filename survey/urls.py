from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'survey'

urlpatterns = [
    url(r'^createSurvey/', views.createSurvey, name="createSurvey"),
    url(r'^takeSurvey/', views.takeSurvey, name="takeSurvey"),
    url(r'^thankyou/', views.thankyou, name="thank-you"),
]
