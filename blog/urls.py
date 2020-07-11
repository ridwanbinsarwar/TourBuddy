from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/', views.new_post, name='new_post'),
    path('detail/<int:id>/', views.view_post, name='view_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),

]
