from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'articles/ping.html')

def pong(request):
    search_data = request.GET.get('search_data')
    context = {
        'search_data':search_data
    }
    return render(request, 'articles/pong.html',context)