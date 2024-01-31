from django.forms import ModelForm
from .models import People
class ParticipantForm(ModelForm):
    class Meta:
        model=People
        fields='__all__'