from django.shortcuts import render
from .models import *

def test(request):
    model = MyModel.objects.get(pk=2)
    return render(request, 'testapp/test.html', {'model': model})
