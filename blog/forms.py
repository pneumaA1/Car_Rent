from .models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    """
        A form to create or update a Commentary instance.
        Attributes:
            model (class): A reference to the Commentary model that this form is associated with.
            fields (tuple): A tuple of field names to include in the form.
    """

    class Meta:
        model = Commentary
        fields = ('author', 'email', 'text')

        name = forms.CharField(label='Name *')
        email = forms.EmailField(label='Email *')
        message = forms.CharField(label='Message', widget=forms.Textarea(
            attrs={'class': 'form-control'}))
