# from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib import messages

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

