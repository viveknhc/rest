from django.urls import path,include
from . import views
appname = "Api"
urlpatterns=[
    path('',views.index,name='index'),
]
# Create your views here.
