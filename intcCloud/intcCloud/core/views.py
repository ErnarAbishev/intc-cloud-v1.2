from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import DocumentForm, DiplomaForm
from .models import Document, DiplomaDocument
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



class Home(TemplateView):
    template_name = 'home.html'

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('signin')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'error_message': 'Login Failed! Enter the username and password correctly'})


def signout(request):
    logout(request)
    return redirect('/')

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {
        'documents': documents
    })

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {
        'form': form
    })

def delete_document(request, pk):
    if request.method == 'POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('document_list')

def diploma_list(request):
    diplomas = DiplomaDocument.objects.all()
    return render(request, 'diploma_list.html', {
        'diplomas': diplomas
    })

def upload_diploma(request):
    if request.method == 'POST':
        form = DiplomaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diploma_list')
    else:
        form = DiplomaForm()
    return render(request, 'upload_diploma.html', {
        'form': form
    })

def delete_diploma(request, pk):
    if request.method == 'POST':
        document = DiplomaDocument.objects.get(pk=pk)
        document.delete()
    return redirect('diploma_list')