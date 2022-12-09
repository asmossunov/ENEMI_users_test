from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from accounts.models import Account


class AccountForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    father_name = forms.CharField(label='Отчество')
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    phone = forms.CharField(label='Номер телефона')

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'father_name', 'email', 'phone', 'password', 'password_confirm')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            # group_name = 'basic_users'
            # group = Group.objects.get(name=group_name)
            # user.groups.add(group)
        return user


class TutorCreationForm(forms.ModelForm):
    place_of_study = forms.CharField(label='Место учёбы')
    working_place = forms.CharField(label='Место работы')

    class Meta:
        model = get_user_model()
        fields = ('place_of_study',
                  'working_place')


class StudyCenterCreationForm(forms.ModelForm):
    study_center_name = forms.CharField(label='Название учебного центра')
    contact_person = forms.CharField(label='Контактное лицо')

    class Meta:
        model = get_user_model()
        fields = ('study_center_name',
                  'contact_person')


