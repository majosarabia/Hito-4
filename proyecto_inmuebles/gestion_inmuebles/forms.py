from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Inmueble

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "rut",
            "tipo_usuario_por_defecto",
        )


class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "tipo_usuario_por_defecto",
        )


class AgregarInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        exclude = ["dueno"]
