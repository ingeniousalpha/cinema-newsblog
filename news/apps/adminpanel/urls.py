from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='loginadmin'),
    path('logout/', views.logout_page, name='logoutadmin'),
    path('article_edit/<art_id>', views.article_edit_page, name='article_edit'),
    path('date_update/<int:art_id>', views.article_date_update, name='date_update'),
]