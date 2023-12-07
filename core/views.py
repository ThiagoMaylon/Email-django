from django.shortcuts import render
from .forms import Emailform
from django.contrib import messages

def index(request):
    forms = Emailform(request.POST or None)
    if str(request.method) == 'POST':
        if forms.is_valid():
            forms.send_email()
            messages.success(request, 'E-mail enviado com sucesso')
            forms = Emailform()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': forms
    }
    return render(request, 'index.html', context)