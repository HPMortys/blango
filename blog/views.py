from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone



# Create your views here.

class IndexView(View):
  def get(self, request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})


class PostDetail(View):
  def get(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request, "blog/post-detail.html", context)

