from django.urls import path
from .import views
urlpatterns = [
    
    # path('',views.index,name='index'),
    path('', views.rule_list, name='rule_list'),
    path('create/', views.rule_create, name='rule_create'),
    path('evaluate/<int:pk>/', views.rule_evaluate, name='rule_evaluate'),
    
]
