from django.urls import path
from . import views

urlpatterns = [
    path('submit_post/', views.submit_post, name='submit_post'),
    path('get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
]
