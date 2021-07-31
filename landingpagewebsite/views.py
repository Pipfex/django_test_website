# Передача содержимого страницы в виде строки, байтовой строки
from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    """Выводит первую страницу проекта."""
    a = '<h1>Hello world!</h1>'
    text = 'Новый текст'
    return render(request, './index.html', {
        'a':a,
        'text':text,
    })