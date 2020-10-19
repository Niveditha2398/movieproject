from django import forms
from moviesapp.models import Moviedetails

class MoviedetailsForm(forms.ModelForm):
    class Meta:
        model = Moviedetails
        fields = ('releasedate','moviename','hero','heroine','rating')