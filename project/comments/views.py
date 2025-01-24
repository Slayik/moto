from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

def comments_page(request):
    # Получаем все комментарии
    comments = Comment.objects.all()

    # Обрабатываем форму
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новый комментарий
            return redirect('comments')  # Перенаправляем на ту же страницу
    else:
        form = CommentForm()

    return render(request, 'main/comments.html', {
        'comments': comments,
        'form': form,
    })
