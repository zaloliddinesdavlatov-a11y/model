from django.urls import path
from . import views
from .models import BookModel


urlpatterns = [
    path('model/', BookModel,),
    path('ber/', views.salom_beruvchi, name='salom_beruvchi'),
    path('mamlakat/', views.mamlakat, name='mamlakat'),
    path('mamlakat/viloyat/', views.viloyat, name='viloyat'),
    path('mamlakat/viloyat/shahar/', views.shahar, name='shahar'),
    path('mamlakat/viloyat/shahar/akademiya/', views.akademiya, name='akademiya'),
]
