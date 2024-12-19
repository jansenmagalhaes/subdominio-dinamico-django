from django.shortcuts import render

def inicio(request):
    organizacao = request.GET.get('organizacao', request.POST.get('organizacao', ''))

    return render(request, 'inicio.html', {'organizacao' : organizacao})

def home(request):
    organizacao = request.GET.get('organizacao', request.POST.get('organizacao', ''))
    
    return render(request, 'home.html', {'organizacao' : organizacao})
