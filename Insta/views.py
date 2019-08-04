from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostListView(ListView):
    model = Post
    template_name = 'test.html'

class PostDetailedView(DetailView):
    model = Post
    template_name = 'post_detail.html'
