from django.urls import path
from . import views


urlpatterns =[
    path('', views.blog_view, name="blog"),
    path('<int:pk>', views.blog_detail_view, name="blog_detail_view"),
]
