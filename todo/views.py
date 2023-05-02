from django.shortcuts import render, get_object_or_404
from .models import TodoItem, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.

def all_posts(request):
    posts = TodoItem.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'todo/index.html', context)

def post_detail_views(request, id):
    post = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.todo = post
            form.save()
            return HttpResponseRedirect(f"/{id}")
    else:
        form = CommentForm()
        comments = post.comments.filter(active=True)
        context = {
            'post': post,
            'id': id,
            'form': form,
            'comments': comments
        }
        return render(request, "todo/todo_detail.html", context)

