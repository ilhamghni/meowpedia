from django.shortcuts import render, redirect, reverse
from main.forms import CatEntryForm
from main.models import CatEntry

from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_home(request):
    
    context = {
        'npm' : '2306201792',
        'name': request.user.username,
        'class': 'PBP E',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "home.html", context)

def create_cat_entry(request):
    form = CatEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        cat_entry = form.save(commit=False)
        cat_entry.user = request.user
        cat_entry.save()
        return redirect('main:show_home')

    context = {'form': form}
    return render(request, "create_cat_entry.html", context)

@csrf_exempt
@require_POST
def create_cat_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    age = strip_tags(request.POST.get("age"))
    description = strip_tags(request.POST.get("description"))
    species = strip_tags(request.POST.get("species"))
    colour = strip_tags(request.POST.get("colour"))

    user = request.user

    new_cat = CatEntry(
        name=name, price=price,
        age=age, description=description,species=species,colour=colour,
        user=user
    )
    new_cat.save()

    return HttpResponse(b"CREATED", status=201)

def edit_cat(request, id):
    cat = CatEntry.objects.get(pk = id)
    form = CatEntryForm(request.POST or None, instance=cat)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_home'))

    context = {'form': form}
    return render(request, "edit_mood.html", context)

def delete_cat(request, id):
    cat = CatEntry.objects.get(pk = id)
    # Hapus cat
    cat.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_home'))


def show_xml(request):
    data = CatEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CatEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# Auth

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_home"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response



from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def create_cat_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_cat = CatEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=data["price"],
            age=data["age"],
            description=data["description"],
            species=data["species"],
            colour=data["colour"]
        )

        new_cat.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)