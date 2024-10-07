from django.forms import ModelForm
from main.models import CatEntry
from django.utils.html import strip_tags

class CatEntryForm(ModelForm):
    class Meta:
        model = CatEntry
        fields = ["name", "price", "age", "description", "species", "colour"]

    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return price 

    def clean_age(self):
        age = self.cleaned_data["age"]
        return age

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_species(self):
        species = self.cleaned_data["species"]
        return strip_tags(species)

    def clean_colour(self):
        colour = self.cleaned_data["colour"]
        return strip_tags(colour)