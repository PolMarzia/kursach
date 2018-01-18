from django.shortcuts import render
from weblab.models import *
from weblab.forms import *
from django.shortcuts import redirect
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import time

# Create your views here.

rec = ['polikarpich14@yandex.ru']

def show_site(request):
    uslugi = Uslugi.objects.filter()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, rec)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            form.save()
            return redirect('show_site')
    return render(request, "index.html", locals())

def buy_usl(request, usl_id):
    uslugi = Uslugi.objects.get(id = usl_id)
    masters = Master.objects.filter()
    if request.method == "POST":
        name = request.POST['firstname']
        tel = request.POST['tel']
        com = request.POST['com']
        try:
            send_mail(name, 'Новый заказaa\nИмя: '+name+'\nТелефон: '+tel+'\nКомментарий: '+com+'\nУслуга: '+uslugi.name, 'IRepair@shop.com', rec)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        time.sleep(0.5)
        return redirect('show_site')
    return render(request, "buy.html", locals())

un = '1'
pw = '2'

def auth_url(request):
    if request.method == "POST":
        global un
        global pw
        un = request.POST['username']
        pw = request.POST['pass']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            return redirect('admin_panel')
        else: 
            return redirect('auth_url')
    return render(request, "admin/auth_url.html", locals())

def admin_panel(request):
    user = auth.authenticate(username=un, password=pw)
    if user is not None:
        uslugi = Uslugi.objects.filter()
        return render(request, "admin/admin_panel.html", locals())
    else:
        return redirect('auth_url')

def add_usl(request):
    user = auth.authenticate(username=un, password=pw)
    if user is not None:
        form = AddUslugaForm()
        if request.method == "POST":
            if 'add' in request.POST.keys() and request.POST['add']:
                form = AddUslugaForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('admin_panel')
            else:
                return redirect('admin_panel')
        return render(request, "admin/add_usl.html", locals())
    else:
        return redirect('auth_url')

def delete_usl(request, usl_id):
    user = auth.authenticate(username=un, password=pw)
    if user is not None:
        uslugi = Uslugi.objects.get(id = usl_id)
        if request.method == "POST":
            if 'yes' in request.POST.keys() and request.POST['yes']:
                uslugi.delete()
                return redirect("admin_panel")
            else:
                return redirect("admin_panel")
        return render(request, "admin/delete_usl.html", locals())
    else:
        return redirect('auth_url')

def edit_usl(request, usl_id):
    user = auth.authenticate(username=un, password=pw)
    if user is not None:
        uslugi = Uslugi.objects.get(id = usl_id)
        form = AddUslugaForm(instance=uslugi)
        if request.method == "POST":
            if 'good' in request.POST.keys() and request.POST['good']:
                form = AddUslugaForm(request.POST, request.FILES, instance=uslugi)
                if form.is_valid():
                    form.save()
                    return redirect("admin_panel")
            else:
                return redirect("admin_panel")
        return render(request, "admin/edit_usl.html", locals())
    else:
        return redirect('auth_url')
