from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request, 'home.html', {'title': 'Web Calculator', 'datetime_now': str(datetime.now())})


def add_numbers_page(request):
    return render(request, 'addnums.html')


def add_numbers(request):
    num_1 = int(request.POST.get('num1'))
    num_2 = int(request.POST.get('num2'))
    result = num_1 + num_2

    return render(request, 'result.html', {'result': result})