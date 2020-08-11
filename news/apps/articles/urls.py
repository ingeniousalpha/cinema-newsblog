from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:art_id>/', views.article_page, name='article_page'),
]
