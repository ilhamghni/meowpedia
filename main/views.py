from django.shortcuts import render

# Create your views here.

def show_home(request):
    context = {
        'npm' : '2306201792',
        'name': 'Ilham Ghani Adrin Sapta',
        'class': 'PBP E'
    }

    cats = {
        'name' : 'kitty',
        'price' : '$20,000',
        'description' : 'fluffy and playfull, does ot like being alone',
        'species' : 'arabian knight',
        'colour' : 'golden brown',
        'age' : '10 year old',
    }

    return render(request, "home.html", {'context' : context, 'cats' : cats})

