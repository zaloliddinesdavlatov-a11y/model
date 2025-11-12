from django.urls import path
from . import views
from .views import kitob_detail


urlpatterns = [
    path('kitoblar/<int:id>/',kitob_detail),
    path('kitob/', views.hamma_kitoblar, name='hamma_kitoblar'),
    path('ber/', views.salom_beruvchi, name='salom_beruvchi'),
    path('mamlakat/', views.mamlakat, name='mamlakat'),
    path('mamlakat/viloyat/', views.viloyat, name='viloyat'),
    path('mamlakat/viloyat/shahar/', views.shahar, name='shahar'),
    path('mamlakat/viloyat/shahar/akademiya/', views.akademiya, name='akademiya'),
]
