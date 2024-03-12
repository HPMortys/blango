from django.urls import path, include 
from . import views

app_name = "blog"
urlpatterns =  [
  path("",  views.IndexView.as_view(), name="main"),
  path("ip/", views.get_ip, name="get-ip"),
  path("post/<slug:slug>", views.PostDetail.as_view(), name="blog-post-detail"),
  path("api/v1/", include("blog.api.urls"),)
]

