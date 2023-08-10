from django.shortcuts import render

def CallebautAcceuil(request):
    return render(request, 'base.html')