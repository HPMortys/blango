from rest_framework import serializers
from django.utils.text import slugify

from blango_auth.models import User
from blog.models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
  tags = serializers.SlugRelatedField(
      slug_field="value", many=True, queryset=Tag.objects.all()
  )

  author = serializers.HyperlinkedRelatedField(
      queryset=User.objects.all(), view_name="api_user_detail", lookup_field="email"
  )

  class Meta:
    model = Post
    # exclude = ["modified_at", "created_at"]
    fields = "__all__"
    readonly = ["modified_at", "created_at"]


  def validate(self, data):
    if not data.get("slug"):
      if data["autogenerate_slug"]:
        data["slug"] = slugify(data["title"])
      else:
        raise serializers.ValidationError("slug is required")
      del data["autogenerate_slug"]
      return data 


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["first_name", "last_name", "email"]