from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from comment.form import CommentForm
from myBlog.models import Post


def post_comment(request, pk):
    article = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = {
                'comment_list': comment_list,
                'article': article,
                'form': form
            }
            return render(request, 'blog/index.html', context=context)
    else:
        redirect(article)