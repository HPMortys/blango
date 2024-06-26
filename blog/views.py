import logging

from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from blog.models import Post
from blog.forms import CommentForm

from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie


logger = logging.getLogger(__name__)
# Create your views here.

def get_ip(request):
  return HttpResponse(request.META['REMOTE_ADDR'])

@method_decorator(cache_page(300), name='dispatch')
@method_decorator(vary_on_cookie, name='dispatch')
class IndexView(View):
  def get(self, request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))
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
      logger.info("Created comment on Post %d for user %s", post.pk, request.user)
      return redirect(request.path_info)


