from django.urls import path
from . import views

#url configuration URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('funds/', views.get_funds),
    path('funds/create/', views.create_fund),
    path('funds/<int:pk>/', views.fund_detail)
]