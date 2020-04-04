from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('test', test_view),
    path('minidatasheet/<slug:ic_name>', minidatasheet_view),
]
