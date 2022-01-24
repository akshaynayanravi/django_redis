from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'title': 'Web Calculator'})


def add_numbers_page(request):
    return render(request, 'addnums.html')


def add_numbers(request):
    num_1 = int(request.GET.get('num1'))
    num_2 = int(request.GET.get('num2'))
    result = num_1 + num_2

    return render(request, 'result.html', {'result': result})