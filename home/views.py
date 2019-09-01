from django.shortcuts import render

# Create your views here.
def render1(req):

    return render(req,'home/index.html')
