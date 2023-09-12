from django import forms


class ProductForm(forms.Form):
    prod_id = forms.IntegerField()
    name = forms.CharField(max_length=100)
    title = forms.CharField(widget=forms.TextInput())
    price = forms.DecimalField()
    count = forms.IntegerField()
    #image = forms.ImageField()
    

class ImageForm(forms.Form):
    image = forms.ImageField()
    
