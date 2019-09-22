from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('home/',  views.index, name='index'),
    path('category/<int:id>/<slug:slug>/',
         views.categry_detail, name='category_detail'),
    path('book/<int:id>/<slug:slug>/',
         views.book_detail, name='book_detail'),
    path('category/<int:id>/<slug:slug>/create-book',
         views.book_create, name='create_book'),
    path('category/<int:id>/book-list',
         views.book_list, name='book_list'),
    path('<int:category_id>/<slug:slug>/delete-book/<int:book_id>',
         views.delete_book, name='delete_book'),
    path('<int:book_id>/read',
         views.read_book, name='read_book'),
]
