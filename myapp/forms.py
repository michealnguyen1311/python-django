from django import forms
from django.forms import ModelForm, Form, TextInput, models, CheckboxInput, Select, widgets, PasswordInput, EmailInput
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField
from django.contrib.auth.models import User
from django.forms.forms import Form
from .models import Place,Restaurant, Waiter

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'   #('name','address','country')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'address': TextInput(attrs={
                'class': 'form-control'
            }),
            'country': TextInput(attrs={
                'class': 'form-control'
            }),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
# Server validation gửi từ Client lên server ( đoạn này đang sai chưa hiểu được)
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Place.objects.get(name=name)
            if not hasattr(self,'instance'):
                return name
            raise ValidationError(f"{name} đã tồn tại. Vui lòng chọn tên khác")
        except Place.DoesNotExist:
            return name
class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'place': Select(attrs={
                'class': 'form-control'
            }),
            'serves_hot_dogs': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pizza': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pho': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
class WaiterForm(ModelForm):
    class Meta:
        model = Waiter
        fields = '__all__'
        widgets = {
            'restaurant': Select(attrs={
                'class': 'form-control'
            }),
            'serves_hot_dogs': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pizza': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'serves_pho': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class RegistrationForm(Form):
    username = CharField(
        label="Tên Đăng Nhập",
        help_text="Tên dùng để đăng nhập vào website",
        max_length="50",
        widget = TextInput(
                attrs={
                'class': 'form-control'
            }   
        )
    )
    password = CharField(
        label="Mật Khẩu",
        widget = PasswordInput(
                attrs={
                'class': 'form-control'
                }   
            )
    )
    confirm_password = CharField(
        label="Mật Khẩu",
        widget = PasswordInput(
                attrs={
                'class': 'form-control'
                }   
            )
    )
    email = EmailField(
        label="Địa chỉ Email",
        widget = EmailInput(
                attrs={
                'class': 'form-control'
                }
        )
    )
    firstname = CharField(
        label="Tên ",
        max_length="50",
        widget = TextInput(
                attrs={
                'class': 'form-control'
            }   
        )
    )
    lastname = CharField(
        label="Ho",
        max_length="50",
        widget = TextInput(
                attrs={
                'class': 'form-control'
            }   
        )
    )
    def clean_username(self):       
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise ValidationError(f"Ten dang nhap {username} đã tồn tại. Vui lòng chọn tên khác")
        except User.DoesNotExist:
            return username
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError(f"Mật khẩu không khớp. Vui lòng nhập lại")
        return confirm_password    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise ValidationError(f"Email {email} đã tồn tại. Vui lòng chọn Email khác")
        except User.DoesNotExist:
            return email
    
    def save_user(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            
            password = self.cleaned_data['password'],
            
            email = self.cleaned_data['email'],
            
            first_name = self.cleaned_data['firstname'],
            last_name = self.cleaned_data['lastname'],
        )
class LoginForm(Form):
    username = CharField(
        label="Tên Đăng Nhập",        
        max_length="50",
        widget = TextInput(
                attrs={
                'class': 'form-control'
            }   
        )
    )
    password = CharField(
        label="Mật Khẩu",
        widget = PasswordInput(
                attrs={
                'class': 'form-control'
                }   
            )
    )