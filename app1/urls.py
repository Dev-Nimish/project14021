from django.urls import path
from app1 import views

app_name = "app1"

urlpatterns = [
    path('', views.if_statement, name = "if_demo"),
    path('if_else/',views.if_else, name = "if_else_demo"),
    path('for/',views.for_loop, name = "for"),
    path('for1/',views.for1, name = "for1"),
]
