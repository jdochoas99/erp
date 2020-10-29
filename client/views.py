from django.shortcuts import render
from .models import Pessoa
# Create your views here.
def index(request):
    return render(request, 'client/index.html',
    {
        'pessoas': Pessoa.objects.all()
    })