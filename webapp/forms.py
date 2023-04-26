"""
This module defines the form used for user registration.
"""

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    """A form for registering a new user.

    This form includes fields for a username, email, and two password inputs
    (with validation to ensure they match and meet minimum requirements),
    as well as optional fields for first and last name.

    Upon submission, the form creates a new User instance with the given
    information, sets their password to the hashed value of the provided
    password, and marks them as active and activated so they can log in.

    Attributes:
        email (EmailField): Required field for the user's email address.
        password1 (CharField): Required field for the user's password.
        password2 (CharField): Required field to confirm the user's password
            matches the first password input.

    Methods:
        clean_password1: Validates the first password input against Django's
            built-in password validators.
        clean: Validates that both password inputs match and calls the
            parent clean method.
        save(commit=True): Overrides the parent save method to create a new
            User instance, set their password, and save them to the database.

    Raises:
        ValidationError: If the password inputs do not match.
    """
    email = forms.EmailField(required=True, label='Your email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (again)',
                                widget=forms.PasswordInput,
                                help_text='Repeat password')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Password mismatch',
                                                   code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name')
