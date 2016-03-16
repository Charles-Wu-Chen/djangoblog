from django import forms


class SearchUserForm(forms.Form):
    userlink = forms.CharField(max_length=100)
