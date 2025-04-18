from django import forms
from articles.models import Articles
class CrearArticulo(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['title', 'description']