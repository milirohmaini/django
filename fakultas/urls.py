from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faperta/', views.faperta, name='faperta'),
    path('feb/', views.feb, name='feb'),
    path('fh/', views.fh, name='fh'),
    path('fisip/', views.fisip, name='fisip'),
    path('fk/', views.fk, name='fk'),
    path('fkip/', views.fkip, name='fkip'),
    path('ft/', views.ft, name='ft'),
    path('maknalambang/', views.maknalambang, name='maknalambang'),
    path('pascasarjana/', views.pascasarjana, name='pascasarjana'),
    path('selayangpandang/', views.selayangpandang, name='selayangpandang'),
    path('strukturorganisasi/', views.strukturorganisasi, name='strukturorganisasi'),
    path('visidanmisi/', views.visidanmisi, name='visidanmisi'),
]