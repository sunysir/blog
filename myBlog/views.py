import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView

from comment.form import CommentForm
from .models import Post, Category, Tag


# Create your views here.
# def index(request):
#     post_list = Post.objects.all()
#     context = {'post_list': post_list}
#     return render(request, 'blog/index.html', context=context)

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 3

# def post(request,pk):
#     article = get_object_or_404(Post, pk=pk)
#     form = CommentForm()
#     article.increase_views()
#     comment_list = article.comment_set.all()
#     article.body = markdown.markdown(article.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
#                                                          'markdown.extensions.toc', ])
#     context = {'article': article, 'form': form, 'comment_list': comment_list}
#     return render(request, 'blog/content.html', context=context)
class PostView(DetailView):
    model = Post
    template_name = 'blog/content.html'
    context_object_name = 'article'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        self.object.increase_views()
        self.object.body = markdown.markdown(self.object.body,
                                         extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                                     'markdown.extensions.toc', ])
        comment_list = self.object.comment_set.all()
        context.update({'form': form, 'comment_list': comment_list})
        return context

# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate)
#     context = {'post_list': post_list}
#     return render(request, 'blog/index.html', context=context)
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)

# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
#     context = {'post_list': post_list}
#     return render(request, 'blog/index.html', context=context)
class ArchivesView(IndexView):
    def get_queryset(self):
        return super().get_queryset().filter(created_time__year=self.kwargs.get('year'), created_time__month=self.kwargs.get('month'))
# def tags(request, pk):
#     tags = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=tags)
#     context = {'post_list': post_list}
#     return render(request, 'blog/index.html', context=context)
class TagsView(IndexView):
    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tags)