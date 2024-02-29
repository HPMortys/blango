from django.urls import path
from . import views

app_name = "blog"
urlpatterns =  [
  path("",  views.IndexView.as_view(), name="main"),
  path("ip/", views.get_ip, name="get-ip"),
  path("post/<slug:slug>", views.PostDetail.as_view(), name="blog-post-detail"),
]

