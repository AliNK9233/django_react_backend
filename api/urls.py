from django.urls import path
from .views import *


urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/create/', create_books, name='create_books'),
    
]
