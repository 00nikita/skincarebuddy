from django.urls import path
from . import views

urlpatterns = [
    path('', views.bos, name='bos'),
    path('skincare/',views.skincare,name='skincare'),
    path('bodycare/',views.bodycare,name='bodycare'),
    path('skincare/combination/',views.combination,name='combination'),
    path('skincare/oilyskin/',views.oilyskin,name='oilyskin'),
    path('skincare/dryskin/',views.dryskin,name='dryskin'),
    path('skincare/sensitiveskin/',views.sensitiveskin,name='sensitiveskin'),

]