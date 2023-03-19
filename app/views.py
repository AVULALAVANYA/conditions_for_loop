from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':1909,'b':2090,'c':42345}
    return render(request, 'condition.html',context=d)
def loop(request):
    d={'name':'lavu'}
    return render(request, 'loop.html',d)
