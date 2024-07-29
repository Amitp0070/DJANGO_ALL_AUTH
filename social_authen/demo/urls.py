from django.urls import path
from demo import views

urlpatterns = [
    path('', views.index),
    # path('social-login/', views.social_login, name='social_login'),
]

