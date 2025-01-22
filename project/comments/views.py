from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def post_detail(request, post_id):
    # Предположим, что у вас есть модель Post
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post, active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
