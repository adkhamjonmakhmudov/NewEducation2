from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'error.html')
