from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<indentification>/', views.change, name='change'),
    path('1/<indentification>/', views.changer, name='changer'),
]