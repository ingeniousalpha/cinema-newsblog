from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='loginadmin'),
    path('article_edit/<art_id>', views.article_edit_page, name='article_edit'),
]