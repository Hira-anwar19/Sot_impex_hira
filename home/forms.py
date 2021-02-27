from django.forms import ModelForm
from django import forms
from .models import Contact, Estimate,Subscribe,Blog,Comment


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class EstimateForm(ModelForm):
    class Meta:
        model = Estimate
        fields ='__all__'

class SubscribeForm(ModelForm):
    class Meta:
        model = Estimate
        fields ='__all__'



class CommentForm(ModelForm):

    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 40, 'cols': 40}))

    class Meta:
        model = Comment
        fields = ['comment']