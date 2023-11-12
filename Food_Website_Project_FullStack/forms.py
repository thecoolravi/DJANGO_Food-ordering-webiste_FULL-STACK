
from django import forms

class usersForm(forms.Form):

    num2 = forms.CharField(required=False) 
    num3 = forms.CharField(label='n2')  
    num4 = forms.CharField(widget=forms.NumberInput()) 
    num5 = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':'email' })) 
    emailia = forms.EmailField(required=False)
    Checkbox = forms.BooleanField()




