from django import forms
from users.models import CustomUser
from django.contrib.auth import authenticate
class Registro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña")

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','phone_number','password']
        widgets={
            'phone_number':forms.NumberInput(),
            'email':forms.EmailInput(),
        }
        help_texts={
            'username':''
        }
    def clean(self):
        
        cleaned_data=super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number=cleaned_data.get('phone_number')
        if phone_number and len(str(phone_number)) > 10:
            raise forms.ValidationError("No se puede")
        email=cleaned_data.get("email")
        username=cleaned_data.get("username")
        usuarios=CustomUser.objects.filter(email=email)
        if usuarios.exists():
            raise forms.ValidationError("El email esta utilizado")
        usuarios=CustomUser.objects.filter(username=username)
        if usuarios.exists():
            raise forms.ValidationError("El nombre de usuario esta siendo utilizado")
        if password != confirm_password:
            raise forms.ValidationError("Las contrasenas no coinciden")
    def save(self, commit=True):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class Login(forms.Form):  # Cambié de ModelForm a Form porque estamos autenticando
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Verifica que el usuario existe y que la contraseña es correcta
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos")
        
        self.user = user

    def get_user(self):
        return self.user
            
        