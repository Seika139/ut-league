from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView


class HelloView(TemplateView):

    def __init__(self):
        self.params = {
        'title': 'Hello',
        'message': 'your data',
        'form': HelloForm(),
        }

    def get(self,request):
        return render(request, 'tdlsite/index.html', self.params)

    def post(self,request):
        self.params['message'] = 'Name : ' + request.POST['name'] + '<br>mail : ' + request.POST['mail'] + '<br>age : ' + request.POST['age']
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'tdlsite/index.html', self.params)
