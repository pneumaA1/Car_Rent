from .models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ('author', 'email', 'text')

        name = forms.CharField(label='Name *')
        email = forms.EmailField(label='Email *')
        message = forms.CharField(label='Message', widget=forms.Textarea(
            attrs={'class': 'form-control'}))
