from django.shortcuts import render

# Create your views here.
def homeView(request):
    if request.method == 'GET':
        return render(request, 'home/index.html', {})