from django.shortcuts import render, redirect   
from main.forms import CatEntryForm
from main.models import CatEntry

from django.http import HttpResponse
from django.core import serializers

def show_home(request):
    cat_entries = CatEntry.objects.all()
    context = {
        'npm' : '2306201792',
        'name': 'Ilham Ghani Adrin Sapta',
        'class': 'PBP E',
        'cat_available' : cat_entries
    }

    return render(request, "home.html", {'context' : context})

def create_cat_entry(request):
    form = CatEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('home:show_home')

    context = {'form': form}
    return render(request, "create_cat_entry.html", context)

def show_xml(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")