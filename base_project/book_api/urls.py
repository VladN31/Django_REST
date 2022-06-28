from django.contrib import admin
from django.urls import path
from book_api.views import BookCreate, BookList, BookDetail
# from book_api.views import book, book_list, book_create

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view())
]
