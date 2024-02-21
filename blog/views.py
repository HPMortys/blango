from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


# Create your views here.

class IndexView(View):
  def get(self, request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

