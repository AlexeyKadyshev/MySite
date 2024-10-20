from django.urls import path
from .views import *

urlpatterns = [path('', index, name='home'),
               path('about/', about, name='about'),
               path('posts/', posts, name='posts'),
               path('write_post/', write_post),
               path('posts/delete/<int:id>', delete_post)]
