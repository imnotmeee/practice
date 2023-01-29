from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer

class PostsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

