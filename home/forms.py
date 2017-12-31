#-*-coding:utf-8 -*-    

from django import forms

class InfoForm(forms.Form):
    mail = forms.EmailField(label=u"")
