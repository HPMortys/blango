from rest_framework import generics 
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework.authentication import TokenAuthentication


class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  authentication_classes = [TokenAuthentication]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]