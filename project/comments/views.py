from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def page_detail(request, page_title):
    # Получаем все активные комментарии для данной страницы
    comments = Comment.objects.filter(page_title=page_title, active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.page_title = page_title  # Устанавливаем название страницы
            new_comment.save()
            return redirect('page_detail', page_title=page_title)
    else:
        comment_form = CommentForm()

    return render(request, 'comments.html', {
        'page_title': page_title,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })
