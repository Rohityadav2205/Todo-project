from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
path('taskentry/', views.form),
path('tasks/', views.alltasks),
path('update/', views.update),
path('delete/', views.delete),
path('previoustask/', views.previoustask),
path('futuretask/', views.futuretask),
path('Between/', views.Between),

]