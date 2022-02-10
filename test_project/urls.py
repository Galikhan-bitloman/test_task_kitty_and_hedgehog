from django.urls import path

from . import views


urlpatterns = [
    path('users/<int:pk>/', views.UserView.as_view()),
    path('kag/', views.KittyandHedgehogView.as_view()),
]