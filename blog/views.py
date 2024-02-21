from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import CommentForm


# Create your views here.

class IndexView(View):
  def get(self, request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})


class PostDetail(View):
  template_name = "blog/post-detail.html"

  def get(self, request, slug):
    post = get_object_or_404(Post, slug=slug)
   

    if request.user.is_active:
      comment_form = CommentForm()
    else: 
      comment_form = None


    context = {"post": post,  "comment_form": comment_form}
    return render(request, self.template_name, context)

  def post(self, request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_active:
      comment_form = CommentForm(request.POST)
    else: 
      comment_form = None
    
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.content_object = post
      comment.creator = request.user
      comment.save()
      return redirect(request.path_info)


