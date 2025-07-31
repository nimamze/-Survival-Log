from django.forms import ModelForm
from .models import Survivor

class SurvivorForm(ModelForm):

    class Meta:
        model = Survivor
        fields = ['username','password','email']
