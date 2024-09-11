from django.forms import ModelForm
from main.models import CatEntry

class CatEntryForm(ModelForm):
    class Meta:
        model = CatEntry
        fields = ["name", "price", "age", "description", "species", "colour"]