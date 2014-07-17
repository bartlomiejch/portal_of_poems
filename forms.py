from django.forms import ModelForm

from poems.models import Poem, Comment, Stropha

from django import forms




class PoemForm(forms.Form):
	title = forms.CharField(max_length=200)
	text = forms.CharField()


class CommentForm(ModelForm):

	class Meta:
		model = Comment
		fileds = ('title', 'text')
		
		
class StrophaAddForm(forms.Form):
	add_stropha = forms.CharField(max_length=200)
