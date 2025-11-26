from django.urls import path
from .views import BookDetailApiView,BookMixedApiView,BookListApiView,BookCreateApiView,BookDeleteApiView,BookEditApiView



urlpatterns=[

    #######
    path('book/',BookListApiView.as_view(),name='book'),
    path('book/create/',BookCreateApiView.as_view(),name='book_create'),
    path('book/edit/<int:pk>/',BookEditApiView.as_view(),name='edit'),
    path('book/delete/<int:pk>/',BookDeleteApiView.as_view(),name='book-delete'),
    path('book/<int:pk>/', BookDetailApiView.as_view(), name='book_detail'),
    path('book/<int:pk>', BookMixedApiView.as_view(), name='book_mixed'),
]