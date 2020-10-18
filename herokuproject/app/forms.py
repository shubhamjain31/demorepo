from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
	username = forms.CharField(required=True,max_length=50,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter UserName'
			}
			))
	email = forms.CharField(required=True,max_length=50,
		widget=forms.EmailInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter Email Id'
			}
			))
	first_name = forms.CharField(required=True,max_length=50,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter First Name',
			}
			))
	last_name = forms.CharField(required=True,max_length=50,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter Last Name'
			}
			))
	password = forms.CharField(required=True,max_length=50,
		widget=forms.PasswordInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter Password'
			}
			))
	confirm_password = forms.CharField(required=True,max_length=50,
		widget=forms.PasswordInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter Confirm Password'
			}
			))

	class Meta():
		model = User
		fields = ['username','email','first_name','last_name','password','confirm_password']

	#unique username validation
	def clean_username(self):
		user = self.cleaned_data['username']
		try:
			match = User.objects.get(username=user)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("Username already exist")

	#email pattern validation
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			mt = validate_email(email)
		except:
			raise forms.ValidationError("Email is not in correct format")
		return email

	def clean_confirm_password(self):
		MIN_LENGTH = 8
		pas = self.cleaned_data['password']
		cpas = self.cleaned_data['confirm_password']
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("Password and Confirm Password not matched")
			else:
				if len(pas) < MIN_LENGTH:
					raise forms.ValidationError("Password should have atleast %d characters"%MIN_LENGTH)
				if pas.isdigit():
					raise forms.ValidationError("Password characters should not all numeric")
		return cpas

class LoginForm(forms.ModelForm):
	username = forms.CharField(required=True,max_length=100,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter User Name'
			}
			))
	password = forms.CharField(required=True,max_length=100,
		widget=forms.PasswordInput(
			attrs={
			'class': 'form-control',
			'placeholder':'Enter Password'
			}
			))
	class Meta():
		model = User
		fields = ['username','password']